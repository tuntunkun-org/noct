#
# SLACKAttachment
#
class Attachment:
	def __init__(self, title, color = None, attachment_type = 'default', actions = []):
		self.title		= title
		self.color		= color
		self.attachment_type	= attachment_type
		self.actions		= actions

	def addAction(self, **dic):
		self.actions.append(dic)

	def to_dict(self):
		return {
			'title'			: self.title,
			'color'			: self.color,
			'attachment_type'	: self.attachment_type,
			'actions'		: self.actions
		}

