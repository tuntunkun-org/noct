
class PlainText:
	def __init__(self, text = None, emoji = True):
		self.type	= 'plain_text'
		self.text	= text
		self.emoji	= emoji

	def to_dict(self):
		return self.__dict__

