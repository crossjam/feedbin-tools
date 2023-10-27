## Starred

See the main [README.md](../README.md) for top level options for
logging and authentication.

<!-- [[[cog
import cog
from feedbin_tools import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["starred", "--help"])
help = result.output.replace("Usage: cli", "Usage: feedbin-tools")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: feedbin-tools starred [OPTIONS]

  Fetch feedbin starred entries for the authed feedbin user and emit as JSON

Options:
  -b, --chunk-size INTEGER
  --extended / --no-extended
  --ids / --no-ids
  --limit INTEGER
  --help                      Show this message and exit.

```
<!-- [[[end]]] -->
