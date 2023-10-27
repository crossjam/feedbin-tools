## Feed

See the main [README.md](../README.md) for top level options for
logging and authentication.

<!-- [[[cog
import cog
from feedbin_tools import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["feed", "--help"])
help = result.output.replace("Usage: cli", "Usage: feedbin-tools")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: feedbin-tools feed [OPTIONS] FEED_ID

  Fetch entries for feedbin feed FEED_ID and emit as JSON

Options:
  --extended / --no-extended
  --limit INTEGER
  --help                      Show this message and exit.

```
<!-- [[[end]]] -->
