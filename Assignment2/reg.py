#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from sys import exit, argv, stdin
from networkHandler import NetworkHandler
from regGUI import runGUI

#-----------------------------------------------------------------------
def main(argv):

	if len(argv) != 3:
		print 'Usage: python %s host port' % argv[0]
		exit(1)

	host = argv[1]
	port = argv[2]

	# Make a new queryHandler to process query requests
	networkHandler = NetworkHandler(host, port)

	# Get our GUI running
	runGUI(networkHandler)

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main(argv)