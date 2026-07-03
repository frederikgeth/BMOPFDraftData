# BMOPF Draft data

This repository collects draft test cases in the BMOPF JSON format, complying 
with the JSON Schema  developed by the IEEE Task Force on *Benchmarking Multiconductor OPF for Distribution Systems*, for up-to-four-wire optimal power flow, currently hosted at
https://github.com/frederikgeth/bmopf-report.

## IEEE PES Task Force

**Benchmarking Multiconductor OPF for Distribution Systems**

| Role | Name | Affiliation |
|---|---|---|
| Chair | Matthew Deakin | Newcastle University, UK |
| Co-chair | Frederik Geth | University of Queensland, Australia |
| Secretary | Amrit Pandey | University of Vermont, USA |

## Motivation and ecosystem

Reliable benchmarks are essential for validating and comparing power system
algorithms, yet unbalanced distribution networks have historically
lacked a common, open benchmark format.  This repository is part of the IEEE
PES Task Force effort to fill that gap — motivated by the success of
community benchmark libraries such as [PGLib](https://power-grid-lib.github.io/)
in the broader power systems and optimisation communities.

BMOPFTools provides the tooling needed to convert real utility-derived OpenDSS
networks into clean, spec-conformant BMOPF benchmark cases, validate them
against the data model, and confirm that they are well-posed OPF instances
before publication. 

Finally, this reports hosts a variety of test cases generated through BMOPFTools.

## Licensing

**Benchmark cases** — the licence is inherited from
each dataset's upstream source and therefore differs **per dataset**. The
matching directories under `/output` are derivatives and carry the same
licence as their source. Every data directory contains a `License.md`/
`license.md` with the exact terms and citation; the licence is also stamped
into each generated case's `meta.license` field.

| Dataset (`test/data/…`) | Licence | Commercial use | Source |
|---|---|---|---|
| `ENWL`, `ENWLvariants` | CC BY 4.0 | yes | CSIRO four-wire LV dataset, [10.25919/jaae-vc35](https://doi.org/10.25919/jaae-vc35) |
| `LV`, `MV`, `Master.dss` (combined), `MVLVmeshed` | **CC BY-NC-SA 4.0** | **no** (non-commercial, share-alike) | CSIRO Australian MV/LV feeder set, [10.25919/ghnz-bk28](https://doi.org/10.25919/ghnz-bk28) |
| `dsuite_networks_scaled_v1.1` | CC BY 4.0 | yes | D-Suite LV networks (Newcastle University), [10.25405/data.ncl.27175317](https://doi.org/10.25405/data.ncl.27175317) |
| `SWER`, `pf_comparison`, small fixtures | CC BY 4.0 | yes | authored for BMOPFTools |

Note that CC BY-NC-SA derivatives must be redistributed under the same
non-commercial/share-alike terms — plan accordingly if you are building a
commercial offering on these cases.

