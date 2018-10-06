#!/usr/bin/env python

#-----------------------------------------------------------------------
# printTableDetails.py
# Author: Michael Li
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# prints out string that has prior length on line of x, without it going
# over
def lineHelper(words, x):

	curLength = x
	line = ""

	for j in range(0, len(words)):

		# if adding this word and a space won't make it too long
		if not (curLength + len(words[j]) + 1 > 72):

			# add word to firstline string, increase length of line,
			line += words[j] + " "
			curLength += len(words[j]) + 1
		else:
			# if it will go over, we want to break
			break

	print line

	if (j != len(words) - 1):
		lineHelper(words[j:], 0)

#-----------------------------------------------------------------------
# prints out every element in a list 
def printHelp(ls):
	for elem in ls:
		print elem

#-----------------------------------------------------------------------
def printAdvanced(dictionary):

	print "Course ID: ", dictionary["courseid"][0]
	print ""

	print "Days: ", dictionary["days"][0]
	print "Start time: ", dictionary["starttime"][0]
	print "End time: ", dictionary["endtime"][0]
	print "Building: ", dictionary["bldg"][0]
	print "Room: ", dictionary["roomnum"][0]
	print ""

	# Handle department stuff
	for cur in dictionary["deptcoursenum"]:
		print "Dept and Number: ", cur

	print ""

	print "Area: ", dictionary["area"][0]
	print ""

	titleWords = dictionary["title"][0].split()

	print "Title: ",
	lineHelper(titleWords, len("Title: "))
	print ""

	descWords = dictionary["descrip"][0].split()
	print "Description: ",
	lineHelper(descWords, len("Description: "))
	print ""

	preqWords = dictionary["prereqs"][0].split()
	print "Prerequisites: ",
	lineHelper(preqWords, len("Prerequisites: "))
	print ""

	# Handle Professors
	for cur in dictionary["profname"]:
		print "Professor: ", cur

#-----------------------------------------------------------------------
# basic output for regdetails
def printBasic(dictionary): 
	
	fields1 = ["courseid", "days", "starttime", "endtime", "bldg", "roomnum"]

	fields2 = ["deptcoursenum"]

	fields3 = ["area", "title", "descrip"]

	fields4 = ["prereqs"]
	
	fields5 = ["profname"]
	
	# aggregated fields of the dictionary, ordered by the way they 
	# should appear in the final output 
	allfields = fields1 + fields2 + fields3 + fields4 + fields5

	for f in allfields: 
		printHelp(dictionary[f])
	

#-----------------------------------------------------------------------
def printOut(dictionary, advanced):

	if advanced:
		printAdvanced(dictionary)
	else:
		printBasic(dictionary)