## Feedmeta

See the main [README.md](../README.md) for top level options for
logging and authentication.

<!-- [[[cog
import cog
from feedbin_tools import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["feedmeta", "--help"])
help = result.output.replace("Usage: cli", "Usage: feedbin-tools")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: feedbin-tools feedmeta [OPTIONS] [FEED_IDS]...

  Retrieve the feed information for each ID in FEED_IDS

  Emit data in JSONL

Options:
  --help  Show this message and exit.

```
<!-- [[[end]]] -->
