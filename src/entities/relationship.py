from .base import BaseElement

class Relationship(BaseElement):
	"""
	A relationship between two entities.
	"""

	def __init__(self, ent1, mul1, mul2, ent2):
		super().__init__()
		self.ent1 = ent1
		self.ent2 = ent2
		self.mul1 = mul1
		self.mul2 = mul2

	def getname(self):
		return '-'.join((self.ent1, self.mul1, self.mul2, self.ent2))
