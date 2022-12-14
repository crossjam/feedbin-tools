# feedbin-tools

[![PyPI](https://img.shields.io/pypi/v/feedbin-tools.svg)](https://pypi.org/project/feedbin-tools/)
[![Changelog](https://img.shields.io/github/v/release/crossjam/feedbin-tools?include_prereleases&label=changelog)](https://github.com/crossjam/feedbin-tools/releases)
[![Tests](https://github.com/crossjam/feedbin-tools/workflows/Test/badge.svg)](https://github.com/crossjam/feedbin-tools/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/crossjam/feedbin-tools/blob/master/LICENSE)

Tools for Working with the Feedbin API

## Installation

Install this tool using `pip`:

    pip install feedbin-tools

## Usage

For help, run:

    feedbin-tools --help

You can also use:

    python -m feedbin_tools --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd feedbin-tools
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
