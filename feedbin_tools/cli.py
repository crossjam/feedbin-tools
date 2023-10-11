import json
import logging
import sys
from pprint import pformat

import click

from .logconfig import DEFAULT_LOG_FORMAT, logging_config

import requests
from requests.auth import HTTPBasicAuth
from requests.utils import parse_header_links

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
@click.option("--user", type=click.STRING, envvar="FEEDBIN_USER")
@click.option("--password", type=click.STRING, envvar="FEEDBIN_PASSWORD")
@click.pass_context
def cli(ctx, log_format, log_level, log_file, user=None, password=None):
    "Tools for Working with the Feedbin API"

    ctx.ensure_object(dict)
    ctx.obj["feedbin_password"] = password
    ctx.obj["feedbin_user"] = user

    logging_config(log_format, log_level, log_file)
    logging.info("FEEDBIN_USER: %s", user)
    if password:
        logging.info("feedbin password provided")
    else:
        logging.info("feedbin password not provided")


def auth_from_context(ctx):
    auth = None
    if ctx.obj["feedbin_user"] and ctx.obj["feedbin_password"]:
        auth = HTTPBasicAuth(ctx.obj["feedbin_user"], ctx.obj["feedbin_password"])
    return auth


@cli.command(name="subscriptions")
@click.pass_context
def subscriptions(ctx):
    """
    Fetch feedbin subscriptions and emit as JSON
    """

    session = requests_cache.CachedSession()
    auth = auth_from_context(ctx)

    resp = session.get("https://api.feedbin.com/v2/subscriptions.json", auth=auth)
    resp.raise_for_status()

    json.dump(resp.json(), sys.stdout)


@cli.command(name="feed")
@click.argument("feed_id")
@click.pass_context
def feed(ctx, feed_id):
    """
    Fetch entries for feedbin feed FEED_ID and emit as JSON
    """

    session = requests_cache.CachedSession()
    auth = auth_from_context(ctx)

    entries_url = f"https://api.feedbin.com/v2/feeds/{int(feed_id)}/entries.json"

    resp = session.get(
        entries_url,
        auth=auth,
        params={"mode": "extended"},
    )
    resp.raise_for_status()

    logging.debug("resp headers:\n %s", pformat(list(resp.headers.items())))

    record_count = int(resp.headers.get("X-Feedbin-Record-Count", -1))
    logging.info("Total records in feed: %s", record_count)

    items = resp.json()

    logging.info("Total records in response: %s", len(items))

    for item in items:
        sys.stdout.write(json.dumps(item) + "\n")

    while "Links" in resp.headers:
        links = parse_header_links(resp.headers["links"])

        resolved_links = {}
        for link in links:
            key = link.get("rel") or link.get("url")
            resolved_links[key] = link

        logging.info("Response pagination: %s", resolved_links)

        if "next" not in resolved_links:
            break

        next_url = resolved_links["next"]["url"]

        logging.info("Fetching next page: %s", next_url)
        resp = session.get(
            next_url,
            auth=auth,
            params={"mode": "extended"},
        )
        resp.raise_for_status()

        items = resp.json()

        logging.info("Total records in response: %s", len(items))

        for item in items:
            sys.stdout.write(json.dumps(item) + "\n")
