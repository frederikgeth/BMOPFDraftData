# Representative French Power Grids: source snapshot

This directory contains all 150 original Roseau multiphase JSON v5 networks and `Cluster_Size.csv` from
[Roseau Technologies' Representative French Power Grids](https://github.com/RoseauTechnologies/Representative_French_Power_Grids), revision `65c1b172c6771ddcb94e2bc9d24d30be19fe78d2`.
The upstream commit is dated 2026-02-13T17:58:15+01:00; this snapshot was imported on 1 October 2026.
All original JSON IDs, coordinates, units and ordering are preserved byte for byte. The cluster-size CSV contains
the number of represented feeders for each representative network.

The dataset is attributed to Seddik Yassine Abdelouadoud and is distributed under
[Etalab Open Licence 2.0](License.md). The producer's [dataset page](https://www.data.gouv.fr/fr/datasets/departs-hta-representatifs-pour-lanalyse-des-reseaux-de-distribution-francais/) provides the original license
declaration and methodological report. The input checksums and exact source links are in `provenance.json`.

Converted models are in [`output/FrenchPowerGrids/original/`](../../../output/FrenchPowerGrids/original/).
The mapping, validation scope and limits are documented in
[`output/FrenchPowerGrids/README.md`](../../../output/FrenchPowerGrids/README.md).
The conversion and validation workflow is in
[`scripts/FrenchPowerGrids/`](../../../scripts/FrenchPowerGrids/).
