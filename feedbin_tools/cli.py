import json
import logging
import sys

import click

from .logconfig import DEFAULT_LOG_FORMAT, logging_config

import requests
import requests_cache


@click.group()
@click.version_option()
@click.option(
    "--log-format",
    type=click.STRING,
    default=DEFAULT_LOG_FORMAT,
    help="Python logging format string",
)
@click.option(
    "--log-level", default="ERROR", help="Python logging level", show_default=True
)
@click.option(
    "--log-file",
    help="Python log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    default=None,
)
def cli(log_format, log_level, log_file):
    "Tools for Working with the Feedbin API"

    logging_config(log_format, log_level, log_file)


@cli.command(name="subscriptions")
def first_command():
    "Command description goes here"

    logging.info("Here's some log output")

    session = requests_cache.CachedSession()
    resp = session.get("https://api.feedbin.com/v2/subscriptions.json")
    resp.raise_for_status()

    json.dump(resp.json(), sys.stdout)
