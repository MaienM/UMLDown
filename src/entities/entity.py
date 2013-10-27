from .base import BaseEntity

class Entity(BaseEntity):
	"""
	An entity.
	"""

	def __init__(self, name):
		super().__init__()
		self.name = name

	def getname(self):
		return self.name
