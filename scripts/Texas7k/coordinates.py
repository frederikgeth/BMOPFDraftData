"""Springfield-style bus coordinate extension, matching the French cases."""
import copy
import math

COORDINATE_FIELDS = ('longitude', 'latitude')


def geographic_bus_points(model):
    points = {}
    for feature in model['extras']['geojson']['features']:
        properties = feature['properties']
        if properties.get('kind') != 'bus':
            continue
        bus_id = properties['id']
        if bus_id in points:
            raise ValueError(f'{bus_id}: duplicate geographic bus feature')
        if feature['geometry']['type'] != 'Point':
            raise ValueError(f'{bus_id}: expected geographic Point geometry')
        coordinates = feature['geometry']['coordinates']
        if not isinstance(coordinates, list) or len(coordinates) != 2:
            raise ValueError(f'{bus_id}: expected [longitude, latitude]')
        for field, value, limit in zip(COORDINATE_FIELDS, coordinates, (180, 90)):
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or not -limit <= value <= limit):
                raise ValueError(f'{bus_id}: invalid {field} in degrees')
        points[bus_id] = coordinates
    return points


def add_bus_coordinates(model):
    points = geographic_bus_points(model)
    # GeoJSON is applied after bus fields by PowerIO; an unknown space there
    # would override the geographic bus interpretation in Tellegen's viewer.
    model['extras']['geojson'].setdefault('powerio_geo', {})['space'] = 'geographic'
    for bus_id, bus in model['bus'].items():
        if bus_id not in points:
            raise ValueError(f'{bus_id}: geographic coordinates missing')
        bus['longitude'], bus['latitude'] = points[bus_id]
    model['meta']['provenance']['bus_coordinates'] = {
        'fields': list(COORDINATE_FIELDS),
        'coordinate_space': 'geographic longitude/latitude in degrees',
        'source': 'extras.geojson bus Point features from OpenDSS Buscoords.dss',
        'internal_bus_locations': 'Copied from a connected original bus; derived locations remain marked in GeoJSON'
    }
    return len(model['bus'])


def electrical_projection(model):
    """Check coordinates, then remove only the two bus extension fields.

    The strict draft BMOPF schema does not declare these fields. Keep every
    other field in the projected document so unrelated schema errors remain
    visible, as in the existing French validation workflow.
    """
    points = geographic_bus_points(model)
    if model['extras']['geojson'].get('powerio_geo', {}).get('space') != 'geographic':
        raise ValueError('Geographic bus coordinates need geographic GeoJSON metadata')
    projected = copy.deepcopy(model)
    for bus_id, bus in projected['bus'].items():
        actual = [bus.get(field) for field in COORDINATE_FIELDS]
        if (bus_id not in points or any(isinstance(value, bool) for value in actual)
                or actual != points[bus_id]):
            raise ValueError(f'{bus_id}: bus coordinates differ from the geographic Point')
        for field in COORDINATE_FIELDS:
            del bus[field]
    return projected, len(projected['bus'])
