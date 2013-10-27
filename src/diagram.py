import shlex
import pydot
from elements import ELEMENTMAP

class Diagram(object):
	"""
	An diagram.
	"""

	def __init__(self):
		self.elements = {}

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
					if entname not in ELEMENTMAP:
						raise Exception('Invalid entity: ' + entname)
					obj = ELEMENTMAP[entname](*shlex.split(rest.strip().strip(':')))
					name = obj.getname()
					if name in self.elements:
						raise Exception('Duplicate entity: ' + name)
					self.elements[name] = obj

	def tographviz(self):
		"""
		Convert to graphviz format.
		"""
		graphelements = [ent.tographviz() for ent in self.elements.values()]
		return 'graph G {{\n{elements}\n}}'.format(elements = '\n\n'.join(graphelements))

	def render(self, fn):
		"""
		Render the diagram.
		"""
		dot = pydot.graph_from_dot_data(self.tographviz())
		dot.write(fn, format='png')

#vim:net:ts=4:sts=4
