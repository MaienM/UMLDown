from PIL import ImageDraw

class BaseElement(object):
	"""
	The base for all drawable elements.
	"""

	def __init__(self):
		pass

	def __str__(self):
		return '<{}: {}>'.format(self.__class__.__name__, self.getname())

	def addline(self, line):
		"""
		Add a line.
		"""
		raise NotImplementedError()

	def getname(self):
		"""
		Get the name of this entity.
		"""
		raise NotImplementedError()

	def tographviz(self):
		"""
		Create a graphviz item for this element.
		"""
		raise NotImplementedError()
