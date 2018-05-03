def odd_even():
	count = 0
	for i in range(1,2001):
		count += 1
		if count %2 == 0:
			print "Number is ", count ,". This is an even number."
		else:
			print "Number is", count,"."," This is an odd number."
odd_even()

def multiply(arr,num):
	for x in range(len(arr)):
		arr[x] *= num 
	return arr
a = [2,4,10,16]
b = multiply(a,5)
print b


def layered_multiples(arr):
	new_array = []
	for x in arr:
		val_arr = []
		for i in range(0,x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

	