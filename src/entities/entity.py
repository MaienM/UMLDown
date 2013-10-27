from .base import BaseElement

class Entity(BaseElement):
	"""
	An entity.
	"""

	def __init__(self, name):
		super().__init__()
		self.name = name
		self.attributes = []

	def getname(self):
		return self.name

	def addline(self, line):
		self.attributes.append(line)

	def tographviz(self):
		return '\t"{name}" [\n\t\tlabel = "{lines}"\n\t\tshape = "record"\n\t]'.format(
			name = self.getname(),
			lines = '|'.join(self.attributes)
		)
