#!/usr/bin/env python

#-----------------------------------------------------------------------
# printTable.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------

# Handle second line of list printing
def _handleSecondLine(words):

	curLength = 0
	line = ""

	for j in range(0, len(words)):

		# if adding this word and a space won't make it too long
		if not (curLength + len(words[j]) + 1 > 44):

			# add word to firstline string, increase length of line,

			line += words[j] + " "
			curLength += len(words[j]) + 1
		else:
			# if it will go over, we want to break
			break

	formatstr = " " * 28 + "{0:<.44s}"

	print formatstr.format(line)
	
	# recursivley call if needed to go onto multiple lines
	if (j != len(words) - 1):
		_handleSecondLine(words[j:])


#-----------------------------------------------------------------------

# Handle case of title running over too long
def _handleTooLong(d, i, divStr):

	# get what our too long title is
	title = d["title"][i]

	# split it into a list
	words = title.split()

	curLength = 0

	firstline = ""

	for j in range(0, len(words)):

		# if adding this word and a space won't make it too long
		if not (curLength + len(words[j]) + 1 > 44):

			# add word to firstline string, increase length of line,

			firstline += words[j] + " "
			curLength += len(words[j]) + 1
		else:
			# if it will go over, we want to stop
			break

	# lets print out the first line, then worry about second line

	# now we need to build out our secondline
	formatstr = "{0:>7s}|{1:>4s}|{2:>9s}|{3:^4s}|{4:<.44s}"

	print formatstr.format(d["classid"][i], d["dept"][i], 
		d["coursenum"][i], d["area"][i], firstline)

	_handleSecondLine(words[j:])

	print divStr




#-----------------------------------------------------------------------

# Basic version of printing - meets assignment specification for output
def printBasic(dictionary):
	
	max_len = len(dictionary[dictionary.keys()[0]])
	for i in range(0, max_len):
		string = ""
		string += dictionary["classid"][i]
		string += '\t' + dictionary["dept"][i]
		string += '\t' + dictionary["coursenum"][i]
		string += '\t' + dictionary["area"][i]
		string += '\t' + dictionary["title"][i]

		print string


#-----------------------------------------------------------------------

# Advanced, "human-readable" version
def printAdvanced(d):

	# Let's have a divider string too
	divStr = '-' * 7 + '+' + '-' * 4 + '+' + '-' * 9 + '+' + '-' * 4

	# b/c ran out of space on earlier line, 45 is to have it extend
	# to the end of the line
	divStr += '+' + '-' * 44


	# Let's make some space at the top from the first call
	print ''

	# Lets start by printing out our categories nicely at the top
	print 'Classid|Dept|Coursenum|Area|Title'

	# followed by dividing string
	print divStr

	max_len = len(d[d.keys()[0]])

	for i in range(0, max_len):

		if len(d["title"][i]) > 44:
			_handleTooLong(d, i, divStr)
			continue

		formatstr = "{0:>7s}|{1:>4s}|{2:>9s}|{3:^4s}|{4:<.44s}"

		print formatstr.format(d["classid"][i], d["dept"][i], 
			d["coursenum"][i], d["area"][i], d["title"][i])

		# end with dividing string
		print divStr




#-----------------------------------------------------------------------

# Handles which version to print based on tag

def printOut(dictionary, advanced):

	if advanced:
		printAdvanced(dictionary)
	else:
		printBasic(dictionary)