def compareLst(lst1,lst2):
	for x in lst1 and lst2:
		if x in lst1 == lst2:
			continue

	if lst1 == lst2:
		print "The lists are identical"
	else:
		print "The lists are not identical"
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareLst(list_one,list_two)
