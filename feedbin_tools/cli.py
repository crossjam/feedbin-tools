import json
import logging
import sys

import click

from itertools import zip_longest

from .logconfig import DEFAULT_LOG_FORMAT, logging_config

import requests
import requests_cache


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


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
def subscriptions():
    "Command description goes here"

    logging.info("Here's some log output")

    session = requests_cache.CachedSession("memory_cache", backend="memory")
    resp = session.get("https://api.feedbin.com/v2/subscriptions.json")
    resp.raise_for_status()

    json.dump(resp.json(), sys.stdout)


@cli.command(name="starred")
def starred():
    "Command description goes here"

    CHUNK_SIZE = 75
    session = requests_cache.CachedSession("memory_cache", backend="memory")
    resp = session.get("https://api.feedbin.com/v2/starred_entries.json")

    resp.raise_for_status()

    starred_ids = resp.json()

    logging.info("Starred entries id count: %d", len(starred_ids))

    for i, chunk in enumerate(
        grouper(starred_ids, CHUNK_SIZE, incomplete="fill", fillvalue=None), 1
    ):
        clean_chunk = [v for v in chunk if v]

    logging.info("Processed %d chunks of size %d or less", i, CHUNK_SIZE)
