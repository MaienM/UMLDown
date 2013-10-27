from PIL import ImageDraw

class Base(object):
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

class BaseEntity(Base):
	"""
	The base for an entity.
	"""

	def getsize(self):
		"""
		Get the size of this element when rendered.
		"""
		raise NotImplementedError()

	def render(self, x, y):
		"""
		Render the entity.
		"""
		raise NotImplementedError()

class BaseRelationship(Base):
	"""
	The base for a relationship.
	"""

	def connects(self):
		"""
		The classes connected by this relationship.
		"""
		raise NotImplementedError()

	def render(self):
		"""
		Render the relationship.
		"""
		raise NotImplementedError()
