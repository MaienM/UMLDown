import sys, os.path, pkgutil

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

def buildentitymap():
	"""
	Build a mapping of all valid entities.
	"""
	entitymap = {}
	for cls in inheritors(getattr(sys.modules['%s.%s' % (__name__, 'base')], 'BaseEntity')):
		if not cls.__name__.startswith('Base'):
			entitymap[cls.__name__.lower()] = cls
	return entitymap

def loadallchildmodules():
	"""
	Load all child modules.
	"""
	for imp, pkgname, _ in list(pkgutil.iter_modules([os.path.dirname(__file__)])):
		fullpkgname = '%s.%s' % (__name__, pkgname)
		if fullpkgname not in sys.modules:
			imp.find_module(pkgname).load_module(fullpkgname)

loadallchildmodules()
ENTITYMAP = buildentitymap()

if __name__ == '__main__':
	print(ENTITYMAP)
