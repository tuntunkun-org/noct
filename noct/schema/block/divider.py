
class Divider:
	def __init__(self):
		self.type = "divider"

	def to_dict(self):
		return self.__dict__

if __name__ == '__main__':
	print(Divider())

