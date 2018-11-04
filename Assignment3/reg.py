#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from sys import exit, argv, stdin, stderr
from networkHandler import NetworkHandler
from regGUI import runGUI

#-----------------------------------------------------------------------
def main(argv):

	if len(argv) != 3:
		print >>stderr, 'Usage: ./reg host port'
		exit(1)

	host = argv[1]

	try:
		port = int(argv[2])
	except ValueError:
		print >>stderr, 'Reg: Port is not an integer'
		exit(1)


	# Make a new queryHandler to process query requests
	networkHandler = NetworkHandler(host, port)

	# Get our GUI running
	runGUI(networkHandler)

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main(argv)