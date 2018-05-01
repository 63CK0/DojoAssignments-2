"""
#if statement:
if <condition>:
	#do something
#if-else statement:
elif <condition>:
	#dosomething
else:
	#do this instead
"""

age = 15
if age >= 18:
	print 'Legal Age'
elif age == 17:
	print 'You are seventeen'

else:
	print 'You are so young!'


for count in range (1,1001):
	print "I will not talk in class", count

#create a new list
#remeber lists can hold many data types, even lists!
my_list = [4, 'dog', 99, ['list', 'in', 'a', 'list'], 6, 7]
for item in my_list:
	print item

count = 0
while count < 5:
	print 'looping - ', count
	count += 1

for val in 'string':
	if val == 'i':
		break
	print val
for val in 'string':
	print val