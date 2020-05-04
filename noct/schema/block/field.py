
class Field:
	def __init__(self):
		self.type	= "section"
		self.fields	= []

	def addField(self, **dict):
		self.fields.append(dict)

	def to_dict(self):
		return self.__dict__

