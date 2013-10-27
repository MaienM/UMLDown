from .base import BaseElement

class Entity(BaseElement):
	"""
	An entity.
	"""

	def __init__(self, name):
		super().__init__()
		self.name = name

	def getname(self):
		return self.name
