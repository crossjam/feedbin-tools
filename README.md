# feedbin-tools

<!--[![PyPI](https://img.shields.io/pypi/v/feedbin-tools.svg)](https://pypi.org/project/feedbin-tools/) --->
<!--- -->
<!--[![Changelog](https://img.shields.io/github/v/release/crossjam/feedbin-tools?include_prereleases&label=changelog)](https://github.com/crossjam/feedbin-tools/releases) --->
[![Tests](https://github.com/crossjam/feedbin-tools/workflows/Test/badge.svg)](https://github.com/crossjam/feedbin-tools/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/crossjam/feedbin-tools/blob/master/LICENSE)

A command line toolkit for working with the [Feedbin HTTP
API](https://github.com/feedbin/feedbin-api/)

Right now we are focused on only reading (GET) from the Feedbin API
for information retrieval, backup, collection, and analysis
purposes. The cli is not intended to be a full fledged Feedbin
client. If motivated, the mutating methods (PUT, POST) may be
implemented in the future.

## Installation

Install this tool using `pip`. Even better use
[`pipx`](https://pypa.github.io/pipx/) which should work perfectly
fine with the URL below:

    pip install git+https://github.com/crossjam/feedbin-tools.git

## Usage

For help, run:

    feedbin-tools --help

You can also use:

    python -m feedbin_tools --help


<!-- [[[cog
import cog
from feedbin_tools import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"])
help = result.output.replace("Usage: cli", "Usage: feedbin-tools")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: feedbin-tools [OPTIONS] COMMAND [ARGS]...

  A command line toolkit for working with the Feedbin HTTP API
  https://github.com/feedbin/feedbin-api/

  Due to the use of the requests library for HTTP, .netrc is honored which is
  another means of setting the HTTP Basic Auth user and password for the feedbin
  endpoints

Options:
  --version          Show the version and exit.
  --log-format TEXT  Python logging format string
  --log-level TEXT   Python logging level  [default: ERROR]
  --log-file FILE    Python log output file
  --user TEXT        feedbin user, also via FEEDBIN_USER envvar
  --password TEXT    feedbin password, also via FEEDBIN_PASSWORD envvar
  --help             Show this message and exit.

Commands:
  entries        Fetch entries for the authed feedbin user and emit as JSON
  feed           Fetch entries for feedbin feed FEED_ID and emit as JSON
  starred        Fetch feedbin starred entries for the authed feedbin user...
  subscriptions  Fetch feedbin subscriptions for the authed feedbin user...

```
<!-- [[[end]]] -->

## Development

To develop this module further, first checkout the code. Then create a new virtual environment:

	git clone +https://github.com/crossjam/feedbin-tools.git
	cd feedbin-tools
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
	
This is a hobby, side (very side) project. I’m grateful for PR
submissions and filed issues, but responses might lag by quite a bit.
