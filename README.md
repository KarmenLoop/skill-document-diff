# Document Diff

English | [简体中文](README.zh-CN.md)

Check what changed between two text versions before approving a revision. Read the line diff alongside the numbers added and removed, so a changed price or deadline is easier to catch.

[Download v0.2.1](https://github.com/KarmenLoop/skill-document-diff/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-document-diff/issues)

## What it does

The example changes delivery from 5 to 3 days and price from 100 to 120 USD. Both number lists and a unified diff show those edits.

This compares plain text, not rendered Word or PDF layout. A numerical change is an observation, not a judgment about whether the revision is acceptable.

![Document Diff sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-document-diff-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-document-diff 0.2.1`. The example changes delivery from 5 to 3 days and price from 100 to 120 USD. Both number lists and a unified diff show those edits.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Supply before and after as text, with optional revision labels. Set max_diff_lines when reviewing a large document, and check truncated before relying on an excerpt.

Compare identical wording with different line endings or a missing final newline. Keep the SHA-256 fields to identify exactly which text versions were checked.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Can it compare scanned PDFs?** Extract and verify the text with a separate tool first. This package has no OCR or PDF reader.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
