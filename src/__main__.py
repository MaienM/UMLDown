#!/usr/bin/python2

import argparse, os.path
from diagram import Diagram

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process UMLDown files.')
	parser.add_argument('file', metavar='FILE', type=str, nargs=1,
			                   help='the file to process')

	args = parser.parse_args()
	fn = args.file[0]

	dia = Diagram()
	dia.parse(fn)
	dia.render(os.path.splitext(fn)[0] + '.png')
