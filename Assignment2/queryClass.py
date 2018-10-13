#!/usr/bin/env python

#-----------------------------------------------------------------------
# queryClass.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
class Query (object):

	def __init__(self, dept=None, coursenum=None, area=None,
			title=None,	h=False):
		self._dept = dept
		self._coursenum = coursenum
		self._area = area
		self._title = title
		self._dict = {}
		self._dict['dept'] = dept
		self._dict['coursenum'] = coursenum 
		self._dict['area'] = area
		self._dict['title'] = title

		self._h = h

	def printOut(self):
		print "Dept: ", self._dept
		print "Coursenum: ", self._coursenum
		print "Area: ", self._area
		print "Title: ", self._title

#-----------------------------------------------------------------------

def _test():
	q1 = Query('cos', '333', 'qr', 'Advanced computing techniques', True)

	# check things are working ok
	print 'Next value should be "cos": ', q1._dept
	print '333: ', q1._coursenum
	print 'qr: ', q1._area
	print 'Advanced computing techniques: ', q1._title
	print 'True :', q1._h

	# check other way works
	q1 = Query(coursenum='123', title='lmao')

	print '123: ', q1._coursenum
	print 'lmao: ', q1._title

	print None
	print q1._area

#-----------------------------------------------------------------------

# if __name__ == '__main__':
# 	_test()

