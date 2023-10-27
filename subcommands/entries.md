## Entries

See the main [README.md](../README.md) for top level options for
logging and authentication.

<!-- [[[cog
import cog
from feedbin_tools import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["entries", "--help"])
help = result.output.replace("Usage: cli", "Usage: feedbin-tools")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: feedbin-tools entries [OPTIONS]

  Fetch entries for the authed feedbin user and emit as JSON

Options:
  --read / --unread
  --starred / --no-starred
  --extended / --no-extended
  --limit INTEGER
  -b, --per-page INTEGER
  --since TEXT                    Return entries after this date
  --include-original / --no-include-original
  --include-enclosure / --no-include-enclosure
  --include-content-diff / --no-include-content-diff
  --help                          Show this message and exit.

```
<!-- [[[end]]] -->
