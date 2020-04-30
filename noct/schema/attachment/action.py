#
# SLACKAction
#
class Action:
	def __init__(self, type, text, url = None):
		self.type	= type
		self.text	= text
		self.url	= url

	def to_dict(self):
		return {
			'type'	: self.type,
			'text'	: self.text,
			'url'	: self.url
		}

