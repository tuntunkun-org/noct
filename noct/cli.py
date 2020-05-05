import os
import click
import requests
from noct.schema import SLACK
from noct.schema.attachment import Attachment, Action

@click.group()
def cmd():
	pass

@cmd.command(name = 'slack')
@click.option('--url', default=lambda: os.environ.get('SLACK_WEBHOOK_URL', None))
@click.argument('channel', required=True)
@click.argument('title', default = '')
@click.argument('username', default = '')
@click.argument('icon_emoji', default = '')
@click.option('--alert', type=click.Choice(['default', 'success', 'warning', 'error']), default = 'default')
@click.option('--buttons', multiple=True)
def slack_cmd(url, channel, title, username, icon_emoji, alert, buttons):
	if url is None:
		raise click.BadOptionUsage('url', 'to pulish slack message, url option or SLACK_WEBHOOK_URL environment variable is required')
	#
	# SLACK 通知用 BASE JSON生成
	#
	slack = SLACK(channel=channel, username=username, icon_emoji=icon_emoji)

	#
	# 表示色の設定
	#
	color = {
		'success': '#7ce87c',
		'warning': '#f0ad4e',
		'error': '#d9534f'
	}.get(alert, None)

	#
	# SLACK Attachment の 作成
	#
	attachment = Attachment(title = title, color = color)

	#
	# SLACK Action の 作成
	#
	for button in buttons:
		if not ':' in button:
			raise click.BadOptionUsage('buttons', 'the button options require a URL followed by a colon after the button name')

		(button_text, button_url) = button.split(':', 1)
		action = Action(type = 'button', text = button_text, url = button_url)
		attachment.addAction(**action.to_dict())

	#
	# JSONの定義
	#
	slack.addAttachment(**attachment.to_dict())
	json = slack.to_dict()

	#
	# リクエストの送信
	#
	r = requests.post(url, json = json)

if __name__ == '__main__':
	cmd()

