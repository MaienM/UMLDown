import shlex
from entities import ENTITYMAP

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
				if line.startswith('#') or len(line.strip()) == 0:
					continue

				# If indented, add to block.
				elif line.startswith(' ') or line.startswith('\t'):
					line = line.strip()
					obj.addline(line)

				# Else, create new object.
				else:
					entname, rest = line.split(None, 1)
					if entname not in ENTITYMAP:
						raise Exception('Invalid entity: ' + entname)
					obj = ENTITYMAP[entname](*shlex.split(rest.strip().strip(':')))
					name = obj.getname()
					if name in self.entities:
						raise Exception('Duplicate entity: ' + name)
					self.entities[name] = obj

	def tographviz(self):
		"""
		Convert to graphviz format.
		"""
		graphentities = [ent.tographviz() for ent in self.entities.values()]
		return 'digraph G {{\n{elements}\n}}'.format(elements = '\n\n'.join(graphentities))

	def render(self):
		"""
		Render the diagram.
		"""

#vim:net:ts=4:sts=4
