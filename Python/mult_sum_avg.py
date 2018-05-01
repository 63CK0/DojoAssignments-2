for x in range (1,1001, 2):
	"""takes a range between 1-1001 and iterates every two numbers
	starting with 1 it would all be odd"""
	print x

for x in range(1,1000001):
	"""between 1 and 100000 if the remainder of x is 5
		x prints, meaning x will always be a multiple
		of 5"""
	if x % 5 ==0:
		print x
		


def sumList(list):
	#This function will take a list and return the sum
	print sum(list);

#calling list/function
list = [1,2,5,10,255,3];

sumList(list);


def avgList(list):
	print sum(list) / len(list)

list = [3,7,8,2,5]

avgList(list)



	


