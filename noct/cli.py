import click
import requests
from noct.schema import SLACK
from noct.schema.attachment import Attachment, Action

@click.group()
def cmd():
	pass

@cmd.command(name = 'slack')
@click.argument('ok', type=click.Choice(['ok', 'error']))
@click.argument('url', required=True)
@click.argument('channel', required=True)
@click.argument('title', default = '')
@click.argument('username', default = '')
@click.argument('icon_emoji', default = ':grinning:')
@click.option('--buttons', '-b', multiple=True)
def slack_cmd(ok, url, channel, title, username, icon_emoji, buttons):
	#
	# SLACK 通知用 BASE JSON生成
	#
	slack = SLACK(channel=channel, username=username, icon_emoji=icon_emoji)

	#
	# SLACK Attachment の 作成
	#
	color = '#FF0000' if ok == 'error' else '#00FF00'
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
	print(json)
	r = requests.post(url, json = json)
	click.echo(r)

if __name__ == '__main__':
	cmd()

