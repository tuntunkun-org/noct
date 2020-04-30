
class Section:
	def __init__(self, text = None):
		self.type	= 'section'
		self.text	= text

	def to_dict(self):
		json = {
			'type'	: self.type
		}

		if not self.text == None:
			json['text'] = {
				'type'	: 'mrkdwn',
				'text'	: self.text
			}
		
		return json

