#this is a comment in python
print "Hello World"
x = "Hello Python"
print x
y = 42
print y

def say_hello(name):
	#these lines are indented therefore part of the function
	if name:
		print 'Hello, ' + name + ' from inside the function'
	else:
		print 'No name'
#now we are outside the function and have ended the previous block
say_hello('Zen')
print 'Outside the function'
first_name = 'Zen'
last_name = 'Coder'
print "My name is {} {}".format(first_name, last_name)
hw = "hello %s" % 'world'
print hw

x = "Hello World"
print x.upper()
"""
    string.count(substring): returns number of occurrences of substring in string.

    string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

    string.find(substring): returns the index of the start of the first occurrence of substring within string.

    string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

    string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
    
    string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
"""