#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from sys import exit, argv, stdin
from networkHandler import QueryHandler
from regGUI import runGUI

#-----------------------------------------------------------------------
def main(argv):

	if len(argv) != 3:
		print 'Usage: python %s host port' % argv[0]
		exit(1)

	host = argv[1]
	port = argv[2]

	# Make a new queryHandler to process query requests
	queryHandler = QueryHandler(host, port)

	# Get our GUI running
	runGUI(queryHandler)

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main(argv)