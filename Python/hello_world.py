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