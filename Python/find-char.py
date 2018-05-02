def compareChar(lst,char):
	new_list = []
	for x in lst:
		if char in x:
			new_list.append(x)
	print new_list
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
compareChar(word_list,char)
			



