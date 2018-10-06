#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Quinn Donohue, Michael Li
#-----------------------------------------------------------------------
from queryClass import Query
from inputreaderDetails import processLine
from SQLExecutor import executeSearchClass
from sys import stderr
from printTableDetails import printOut
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
		search = processLine(argv)

		# Pass query to our SQL executor, who returns a dict
		# encapsulating the values
		found = executeSearchClass(search._classid)

		# Pass dict to our printOut function, along with bool that
		# indicates if it should be human readable or not
		printOut(found, search._h)

		# Catch exceptions, print out the appropriate error message
		# preceeded with "reg: "
	except Exception, e:
		print >>stderr, 'regdetails:',
		print >>stderr, e


#-----------------------------------------------------------------------

if __name__ == '__main__':
	_main(argv)