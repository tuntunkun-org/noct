import os
import click
import requests
from noct.schema import SLACK
from noct.schema.attachment import Attachment, Action

@click.group()
def cmd():
	pass

@cmd.command(name = 'slack')
@click.option('--url', default=lambda: os.environ.get('SLACK_URL', None))
@click.argument('channel', required=True)
@click.argument('title', default = '')
@click.argument('username', default = '')
@click.argument('icon_emoji', default = ':grinning:')
@click.option('--alert', type=click.Choice(['default', 'success', 'warning', 'error']), default = 'default')
@click.option('--buttons', multiple=True)
def slack_cmd(url, channel, title, username, icon_emoji, alert, buttons):
	if url is None:
		raise click.BadOptionUsage('url', 'to pulish slack message, url option or SLACK_URL environment variable is required')
	#
	# SLACK 通知用 BASE JSON生成
	#
	slack = SLACK(channel=channel, username=username, icon_emoji=icon_emoji)

	#
	# 表示色の設定
	#
	color = None
	if alert == 'success':
		color = '#7ce87c'
	if alert == 'warning':
		color = '#f0ad4e'
	if alert == 'error':
		color = '#d9534f'

	#
	# SLACK Attachment の 作成
	#
	attachment = Attachment(title = title, color = color)

	#
	# SLACK Action の 作成
	#
	for button in buttons:
		tmp = button.split(':', 1)
		button_text = tmp[0]
		button_url = tmp[1]
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

