
class Query(object):
	"""Defines query object type"""

	def __init__(self, number, name, code, desc, usage):
		self.number = number
		self.name = name
		self.code = code
		self.desc = desc
		self.usage = usage

	def __str__(self):
		return ("Number: {}\n"
			"Name: {}\n"
			"Code: {}\n"
			"Description: {}\n"
			"Usage: {}").format(self.number, self.name, self.code, self.desc, self.usage)
			








