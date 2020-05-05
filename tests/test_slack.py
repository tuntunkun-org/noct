import os
import click
import mock
from click.testing import CliRunner
from noct.cli import slack_cmd

SLACK_WEBHOOK_URL_VALID = 'https://slack/webhook/valid'
SLACK_WEBHOOK_URL_INVALID = 'https://slack/webhook/invalid'
SLACK_CHANNEL = 'channel'

runner = CliRunner()

def mock_request_post(url, json):
	pass


def test_slack_cmd():
	result = runner.invoke(slack_cmd)
	assert result.exit_code == 2

	result = runner.invoke(slack_cmd, ['slack', 'channel'])
	assert result.exit_code == 2


@mock.patch('requests.post', side_effect=mock_request_post)
def test_slack_url_with_arg(mock_post):

	result = runner.invoke(slack_cmd, ['slack', 'channel', '--url'])
	assert result.exit_code == 2

	result = runner.invoke(slack_cmd, ['slack', 'channel', '--url', SLACK_WEBHOOK_URL_VALID])
	mock_post.assert_called_once_with(SLACK_WEBHOOK_URL_VALID, json=mock.ANY)



@mock.patch('requests.post', side_effect=mock_request_post)
def test_slack_url_with_env(mock_post):
	result = runner.invoke(slack_cmd, ['slack', 'channel'])
	assert result.exit_code == 2

	with mock.patch.dict(os.environ, {'SLACK_WEBHOOK_URL': SLACK_WEBHOOK_URL_VALID}):
		result = runner.invoke(slack_cmd, ['slack', 'channel'])
		mock_post.assert_called_once_with(SLACK_WEBHOOK_URL_VALID, json=mock.ANY)


@mock.patch('requests.post', side_effect=mock_request_post)
def test_slack_url_with_env_and_arg(mock_post):

	result = runner.invoke(slack_cmd, ['slack', 'channel', '--url'])
	assert result.exit_code == 2

	with mock.patch.dict(os.environ, {'SLACK_WEBHOOK_URL': SLACK_WEBHOOK_URL_INVALID}):
		result = runner.invoke(slack_cmd, ['slack', 'channel', '--url', SLACK_WEBHOOK_URL_VALID])
		mock_post.assert_called_once_with(SLACK_WEBHOOK_URL_VALID, json=mock.ANY)


@mock.patch('requests.post', side_effect=mock_request_post)
def test_slack_with_buttons_option(mock_post):
	with mock.patch.dict(os.environ, {'SLACK_WEBHOOK_URL': SLACK_WEBHOOK_URL_VALID}):
		result = runner.invoke(slack_cmd, ['slack', 'channel', '--button'])
		assert result.exit_code == 2

		result = runner.invoke(slack_cmd, ['slack', 'channel', '--button', 'ok'])
		assert result.exit_code == 2

		result = runner.invoke(slack_cmd, ['slack', 'channel', '--buttons', 'ok:https://www.google.com/'])
		assert result.exit_code == 0

		result = runner.invoke(slack_cmd, ['slack', 'channel', '--buttons', 'ok:https://www.google.com/', '--buttons', 'ng'])
		assert result.exit_code == 2

