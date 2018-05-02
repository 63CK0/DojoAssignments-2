mixedl = ['magical unicorns',19,'hello',98.98,'world']
numList = []
strList = []

def listType(lst):
	empty_string = ''
	total = 0
	for x in lst:
		if isinstance(x,int) or isinstance(x,float):
			total += x
		elif isinstance(x,str):
			empty_string += x
	if empty_string and total:
		print "This list you entered is of mixed type"
		print "String: ", empty_string
		print "Sum: ", total
	elif total:
		print "The list you entered is of integer type"
		print "Sum: ", total
	else:
		print "The list you entered is of string type"
		print "String: ", empty_string

listType(mixedl)