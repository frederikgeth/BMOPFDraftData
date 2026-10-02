"""Download only the 62 vetted p1uhs0_1247 source files and verify their SHA-256 hashes."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse, hashlib, json, urllib.parse, urllib.request
PREFIX = 'SMART-DS/v0.9/2016/Full_Texas/P1U/scenarios/base_timeseries/opendss/p1uhs0_1247/'
BASE = 'https://oedi-data-lake.s3.amazonaws.com/'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    rows = json.loads(args.manifest.read_text())
    assert len(rows) == 62 and sum(row['size'] for row in rows) < 20_000_000
    root = args.destination.resolve()

    def get(row):
        assert row['key'] == PREFIX + row['path']
        dest = (root / row['path']).resolve()
        assert dest.is_relative_to(root)
        if dest.exists():
            assert hashlib.sha256(dest.read_bytes()).hexdigest() == row['sha256']
            return
        data = urllib.request.urlopen(BASE + urllib.parse.quote(row['key']), timeout=60).read()
        assert len(data) == row['size'] and hashlib.sha256(data).hexdigest() == row['sha256']
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(get, rows))
    print(f'Verified {len(rows)} source files in {root}')


if __name__ == '__main__':
    main()
