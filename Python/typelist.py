l = ['magical unicorns',19,'hello',98.98,'world']
numList = []
strList = []

def type(object):
	for x in object:
		if x < len(object):
			if object is int:
				numList.append(object)
			elif object is str:
				strList.append(object)

	print sum(numList)
	print ' '.join(strList)
type(l)