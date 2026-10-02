# Texas7k pilot source

The `p1uhs0_1247/` directory preserves all 62 downloaded OpenDSS files unchanged.
`source_manifest.json` records their S3 keys, byte sizes and SHA-256 hashes.
The original masters reference external annual profiles, which are not included;
the nominal-snapshot adapter does not require them.

The source follows the OEDI registry's CC BY 3.0 US license; see [License.md](License.md)
and [SOURCE_NOTICE.md](SOURCE_NOTICE.md) for upstream attribution and evidence.
See [the workflow README](../../../scripts/Texas7k/README.md) for hash verification,
optional re-download, conversion and validation commands.
