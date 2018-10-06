
from searchClass import Search 

def isInteger(val):
	try: intresult = int(val)
	except ValueError: return False
	return True

def _processList(args):

	keys = {'-h': False, 'classid': None}	

	# if no inputs then the only error can be missing classid 
	if len(args) == 0: 
		raise Exception("missing classid")
 
 	# if one input, make sure classid is integer; if it is save  
	elif len(args) == 1:
		val = args[0]
		if not isInteger(val):
			raise Exception("classid is not an integer")
		else: 
			keys['classid'] = val
	else:
		if isInteger(args[0]):
			raise Exception("too many arguments")
		else: 
			if args[0] != '-h':
				raise Exception ("classid is not an integer")
			else: 
				if isInteger(args[1]):
					keys['-h'] = True
					keys['classid'] = args[1]
                                        if len(args) > 2:
                                                raise Exception("too many arguments")
				else: 
					raise Exception("classid is not an integer")
	return keys 

def _createSearch(keys):
	return Search(keys['-h'], keys['classid'])

def processLine(args):
	words = args[1:]
	keys = _processList(words)
	return _createSearch(keys)
