import click
from click.testing import CliRunner
from noct.cli import cmd

runner = CliRunner()

def test_noct_cmd():
	result = runner.invoke(cmd)
	assert result.exit_code == 0

def test_noct_unknown_subcommand():
	result = runner.invoke(cmd, ['unknown'])
	assert result.exit_code == 2
