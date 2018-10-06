#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------
from queryClass import Query
from inputreader import processLine
from SQLExecutor import executeSearch
from sys import stderr
from printTable import printOut
from sys import argv
#-----------------------------------------------------------------------

# Main function. Will repeatedly read in lines, execute SQl search,
# and then print out return values. It will catch errors and print
# an appropriate error message

def _main(argv):

		# Try-except loop, so if exceptions are thrown we catch them and
		# can continue executing queries afterwards
	try:
		# Read in a line, get our query
		query = processLine(argv)

		# Pass query to our SQL executor, who returns a dict
		# encapsulating the values
		found = executeSearch(query)

		# Pass dict to our printOut function, along with bool that
		# indicates if it should be human readable or not
		printOut(found, query._h)

		# Catch exceptions, print out the appropriate error message
		# preceeded with "reg: "
	except Exception, e:
		print >>stderr, 'reg:',
		print >>stderr, e


#-----------------------------------------------------------------------

if __name__ == '__main__':
	_main(argv)