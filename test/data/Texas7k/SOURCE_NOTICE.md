# Texas7k / SMART-DS source and licensing evidence

This is a conversion pilot of the publicly supplied synthetic substation
`p1uhs0_1247`, downloaded on 2026-10-02 from:

`s3://oedi-data-lake/SMART-DS/v0.9/2016/Full_Texas/P1U/scenarios/base_timeseries/opendss/p1uhs0_1247/`

The [Texas7k transmission/distribution dataset page](https://electricgrids.engr.tamu.edu/texas7k-td/)
provides this exact substation prefix as its example. The 62 files in the source
subfolder remain byte-for-byte unchanged. The adjacent manifest records their
S3 keys, sizes and SHA-256 hashes. External annual profile CSVs were not fetched.

Please retain the upstream attribution and cite:

C. Mateo, F. Postigo, T. Elgindy, A. Birchfield, P. Duenas, B. Palmintier,
N. Panossian, T. Gomez, F. de Cuadra, T. Overbye, F. Safdarian, and D. Wallison,
“Building and validating a large-scale combined transmission & distribution
synthetic electricity system of Texas,” International Journal of Electrical
Power and Energy Systems, vol. 159, Aug. 2024.

The source page requests this research citation. These conversions are
independent modifications and carry no upstream endorsement.

## License evidence, checked 2026-10-02

- The [OEDI AWS registry](https://registry.opendata.aws/oedi-data-lake/) lists
  [CC BY 3.0 United States](https://creativecommons.org/licenses/by/3.0/us/)
  and includes the SMART-DS bucket prefix.
- The [SMART-DS OEDI submission 2981](https://data.openei.org/submissions/2981)
  links to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), but its
  description explicitly concerns SFO, GSO and AUS; it does not establish
  the license of the Full_Texas/v0.9 files.
- The Texas7k T&D source page identifies the exact public S3 source and
  requests the research citation above; it does not state a different license.

This package follows the published OEDI registry license: **Creative Commons
Attribution 3.0 United States**, identifier `CC-BY-3.0-US`. This is the license
basis for the unchanged source, converted BMOPF model and derived validation
data/figures; it is not a claim that the Texas7k page itself names a CC version.
See [License.md](License.md) and the [legal code](https://creativecommons.org/licenses/by/3.0/us/legalcode).
CC BY 4.0 is not inferred from the submission for other regions.

Derivative conversion and validation work: Frederik Geth, 2026. Retain source
attribution, these links, and the modifications below. No upstream endorsement
is implied. The conversion scripts have a separate MIT license.

## Modifications

The derivative is a fixed nominal-load PF snapshot: yearly references are
removed from the working copy; OpenDSS regulator taps are solved and frozen;
disabled switches are excluded and closed switches retain their effective
finite impedance as lines; three-winding split-phase transformers use exact
leakage-star equivalents; tap-dependent series impedances are rescaled to
BMOPF's single tap-ratio convention. Continuous current limits use OpenDSS
NormAmps; the effective emergency ratings remain in the parameter archive.

Original geographic coordinates are retained. Internal star/source buses
inherit a connected original bus's coordinates and are marked as derived.
Source neutral/ground conventions and reduced matrices are retained. No
new Kron reduction, explicit-neutral reconstruction, annual profile sampling,
OPF objective or inferred voltage bound is introduced. OpenDSS numerical
anti-floating transformer shunts are not equipment and are omitted from the
BMOPF model; their small effect is quantified in the validation report.
