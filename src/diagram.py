#!/usr/bin/python

from entities import entitymap

class Diagram(object):
	"""
	An diagram.
	"""

	def __init__(self):
		self.entities = {}

	def parse(self, fn):
		"""
		Parses an UMLDown file.
		"""
		with open(fn, 'r') as f:
			obj = None
			for line in f:
				# Ignore comments and empty lines.
				if line.startswith('#') or len(line.trim()) == 0:
					continue

				# If indented, add to block.
				if line.startswith(' ') or line.startswith('\t'):
					line = line.trim()
					if line.endswith('()'):
						obj.functions.append(line)
					else:
						obj.attributes.append(line)

				# Else, create new object.
				entname, name = line.split(None, 1)
				if entname not in entitymap:
					raise Exception('Invalid entity: ' + entname)
				obj = self.entities[name] = entitymap[entname](name)

	def render(self):
		"""
		Render the diagram.
		"""

	def position(self):
		"""
		Position the entities.
		"""

#vim:net:ts=4:sts=4
