#
# SLACK
#
class SLACK:
	def __init__(self, channel, username = 'SLACK', icon_emoji = ':grin:'):
		self.channel		= channel
		self.username		= username
		self.icon_emoji		= icon_emoji
		self.attachments	= []
		self.blocks		= []

	def addAttachment(self, **dic):
		self.attachments.append(dic)

	def addBlock(self, **dic):
		self.blocks.append(dic)

	def to_dict(self):
		return {
			'channel'	: self.channel,
			'username'	: self.username,
			'icon_emoji'	: self.icon_emoji,
			'attachments'	: self.attachments,
			'blocks'	: self.blocks
		}

