#!/usr/bin/python

import sys

class BaseElement(object):
	"""
	The base for all drawable elements.
	"""

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

class Entity(BaseElement):
	"""
	An entity.
	"""

	def __init__(self, name):
		self.name = name
		self.attributes = []

	def getname(self):
		return self.name

	def addline(self, line):
		self.attributes.append(line)

	def tographviz(self):
		return '\t"{name}" [\n\t\tlabel = "{{{name}|{lines}}}"\n\t\tshape = "record"\n\t]'.format(
			name = self.getname(),
			lines = '\\n'.join(self.attributes)
		)

class Relationship(BaseElement):
	"""
	A relationship between two entities.
	"""

	def __init__(self, ent1, mul1, mul2, ent2):
		self.ent1 = ent1
		self.ent2 = ent2
		self.mul1 = mul1
		self.mul2 = mul2

	def getname(self):
		return '-'.join((self.ent1, self.mul1, self.mul2, self.ent2))

	def tographviz(self):
		return '\t"{first}" -- "{second}" [\n\t\theadlabel="{firstmul}"\n\t\ttaillabel="{secondmul}"\n\t]'.format(
			first = self.ent1,
			firstmul = self.mul2,
			second = self.ent2,
			secondmul = self.mul1
		)

def inheritors(cls):
	"""
	Get all (direct and indirect) subclasses of cls. 
	"""
	subclasses = set()
	work = [cls]
	while work:
		parent = work.pop()
		for child in parent.__subclasses__():
			if child not in subclasses:
				subclasses.add(child)
				work.append(child)
	return subclasses

ELEMENTMAP = dict([(cls.__name__.lower(), cls) for cls in inheritors(BaseElement)])
