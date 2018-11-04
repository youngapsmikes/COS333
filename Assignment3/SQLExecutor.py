from os import path 
from sys import argv, stderr, exit 
from sqlite3 import connect 
from collections import defaultdict 
from queryClass import Query 

def removeWildCard(str, wildcard_list):
	str_list = list(str)
	for c in wildcard_list: 
		if c in str_list:
			idx = str_list.index(c)
			new_list = str_list[0:idx] + ['[',c,']'] + str_list[idx+1:]
			str_list = new_list 

	return "".join(str_list)

def keyValid(query, cursor, classid):
	
	cursor.execute(query, [classid])
	row = cursor.fetchone()
	
	if row is None: 
		return False

	return True 

# given a query object return a list 
def executeSearch(q1):

	database_name = 'reg.sqlite'

	if not path.isfile(database_name):
			raise Exception('database reg.sqlite not found')
	
	connection = connect(database_name)
	cursor = connection.cursor() 
	
	queryStr = 'SELECT classes.classid, crosslistings.dept, crosslistings.coursenum, courses.area, courses.title' + \
			' FROM classes, crosslistings, courses' + \
			' WHERE classes.courseid = crosslistings.courseid AND classes.courseid = courses.courseid' + \
			' AND courses.area LIKE ?' + \
			' AND crosslistings.coursenum LIKE ?' + \
			' AND crosslistings.dept LIKE ?' + \
			' AND courses.title LIKE ?' + \
			' ORDER BY crosslistings.dept, crosslistings.coursenum, classes.classid'

	## create the query list to pass into cursor 
	query_list = []
	for i in range(0, len(q1._dict)): 
		query_list.append("")

	for idx,elem in enumerate(sorted(q1._dict.keys())):
		## if there is no corresponding condition 
		## for an AND fill in with the match all
		value = q1._dict[elem]
		if value is None:
			query_list[idx] = "%"
		else:
			if '%' in value or '_' in value:
				value = removeWildCard(value, ['%', '_'])
			query_list[idx] = "%" + value + "%"

	cursor.execute(queryStr, query_list)
	row = cursor.fetchone()

	fields = ["classid", "dept", "coursenum", "area", "title"]
	dictionary = {}

	for f in fields:
		dictionary[f] = list()

	# rows_list = []
	# rows_list.append(fields)

	while row is not None:
		#rows_list.append(row)
		for idx, r in enumerate(row):
			dictionary[fields[idx]].append(str(row[idx]))

		row = cursor.fetchone()

	# # while we still have valid line print lines #
	# while row is not None: 
	# 	for r in row:
	# 		print str(r),
	# 	print ""
	# 	row = cursor.fetchone()
	cursor.close()
	connection.close()

	return dictionary

def executeSearchClass(classid):

	database_name = 'reg.sqlite'

	if not path.isfile(database_name):
			raise Exception('database reg.sqlite not found')
	
	connection = connect(database_name)
	cursor = connection.cursor() 
	
	queryStr0 = "SELECT classes.courseid FROM Classes where classes.classid = ?"

	queryStr1 = "SELECT classes.courseid, classes.days, classes.starttime," + \
	"classes.endtime, classes.bldg, classes.roomnum FROM classes WHERE classes.classid = ?"

	queryStr2 = "SELECT crosslistings.dept, crosslistings.coursenum FROM crosslistings, classes" + \
	" WHERE crosslistings.courseid = classes.courseid AND classes.classid = ?" + \
	" ORDER BY crosslistings.dept, crosslistings.coursenum"

	queryStr3 = "SELECT courses.area, courses.title, courses.descrip FROM courses, classes" + \
	" WHERE courses.courseid = classes.courseid AND classes.classid = ?"

	queryStr4 = "SELECT courses.prereqs FROM courses, classes" + \
	" WHERE courses.courseid = classes.courseid AND classes.classid = ?"

	queryStr5 = "SELECT profs.profname FROM profs, classes, coursesprofs" + \
	" WHERE profs.profid = coursesprofs.profid" + \
	" AND coursesprofs.courseid = classes.courseid AND classes.classid = ?" + \
        " ORDER BY profs.profname" 

	if not keyValid (queryStr0, cursor, classid):
		raise Exception("classid does not exist")

	fields1 = ["courseid", "days", "starttime", "endtime", "bldg", "roomnum"]
	dictionary = {}
	dictionary = addtoDictionary(dictionary, fields1, cursor, queryStr1, classid)

	fields2 = ["dept", "coursenum"]
	dictionary = addtoDictionary(dictionary, fields2, cursor, queryStr2, classid)

	fields3 = ["area", "title", "descrip"]
	dictionary = addtoDictionary(dictionary, fields3, cursor, queryStr3, classid)
	fields4 = ["prereqs"]
	dictionary = addtoDictionary(dictionary, fields4, cursor, queryStr4, classid)	

	fields5 = ["profname"]
	dictionary = addtoDictionary(dictionary, fields5, cursor, queryStr5, classid)	

	dictionary["deptcoursenum"] = map(lambda (x,y): x + " "+ y, zip(dictionary["dept"], dictionary["coursenum"]))
		
	return dictionary 

def addtoDictionary(dictionary, fields, cursor, query, classid):
	
	cursor.execute(query, [classid])
	row = cursor.fetchone()

	for f in fields:
		dictionary[f] = list()

	while row is not None:
		for idx, r in enumerate(row):
			dictionary[fields[idx]].append(str(row[idx]))

		row = cursor.fetchone()
	return dictionary 

def main():
	
	dictionary = executeSearchClass(9032)	
	printBasicDetails(dictionary)

if __name__ == '__main__':
	main()
