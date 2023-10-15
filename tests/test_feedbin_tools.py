from click.testing import CliRunner
from feedbin_tools.cli import cli


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_subcommands_exist():
    subcommands = ["feed", "starred", "subscriptions"]

    runner = CliRunner()
    with runner.isolated_filesystem():
        for subcommand in subcommands:
            result = runner.invoke(cli, [subcommand, "--help"])
            assert result.exit_code == 0
