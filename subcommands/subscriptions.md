## Subscriptions

See the main [README.md](../README.md) for top level options for
logging and authentication.

<!-- [[[cog
import cog
from feedbin_tools import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["subscriptions", "--help"])
help = result.output.replace("Usage: cli", "Usage: feedbin-tools")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: feedbin-tools subscriptions [OPTIONS]

  Fetch feedbin subscriptions for the authed feedbin user and emit as JSON

Options:
  --since TEXT                Return entries after this date
  --extended / --no-extended  Include extended information
  --help                      Show this message and exit.

```
<!-- [[[end]]] -->
