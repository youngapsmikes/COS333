#!/usr/bin/env python

#-----------------------------------------------------------------------
# inputreader.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from queryClass import Query
from sys import stdin, stderr


#-----------------------------------------------------------------------

# Taking in keys, create query
def _createQuery(keys):
	return Query(keys['-dept'], keys['-coursenum'], keys['-area'],
		keys['-title'], keys['-h'])

#-----------------------------------------------------------------------

def otherKeys(dictionary):
	for key in dictionary: 
		if key == '-h':
			continue
		else: 
			if dictionary[key] != None:
				return True
	return False

# Process list of words to output dict with key/ value pairs, updating
# dictionary with key value pairs and handling exceptions
def _processList(words):

	# set up so we can search through. Index will be 0 to start,
	# and validKeys shows what is allowed
	index = 0
	keys = {'-h': False, '-dept': None, '-coursenum': None,
	'-area': None, '-title': None}

	while index < len(words):
		key = words[index]

		# increment our index
		index = index + 1

		# Check it's a valid key
		if not key in keys:
			raise Exception('invalid key')


		if key == '-h':
			# if alrady have a h flag
			if keys.get(key):
				raise Exception('invalid key')

			# otherwise lets update, continue on
			if otherKeys(keys):
				raise Exception('invalid key')
			keys[key] = True

			continue

		# Check it's not a duplicate
		if keys.get(key):
			raise Exception('duplicate key')

		# if we are at end of words list
		if index == len(words):
			raise Exception('missing value')

		value = words[index].lower()

		# update dictionary since no problems
		keys[key] = value

		# increment our index again
		index = index + 1

	return keys

#-----------------------------------------------------------------------

# Read in line from stdin, return list of words
# outdated
def _readIn():
	arguments = stdin.readline()
	return arguments.split()


#-----------------------------------------------------------------------

# Execute our processLine - read in a line, convert it to a query object
# throwing appropriate exceptions as needed
# edited by Michael Li 3:29 pm
def processLine(args):
	words = args[1:]
	keys = _processList(words)
	return _createQuery(keys)

#-----------------------------------------------------------------------

# Tests by reading in and printing out output
# outdated.
def _test():

	# Let's test our processLine, write out as needed
	while True:
		try:
			q1 = processLine()

			# print out values
			print 'Department: ', q1._dept
			print 'Course Number: ', q1._coursenum
			print 'Area: ', q1._area
			print 'Title: ', q1._title
			print 'H tag:', q1._h

		except Exception, e:
			print >>stderr, 'reg: ',
			print >>stderr, e



#-----------------------------------------------------------------------
if __name__ == '__main__':
	_test()