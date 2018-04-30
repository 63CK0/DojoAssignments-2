words = "It's thanksgiving day. It's my birthday,too!"
words.find('day')
print words.replace('day','month')


x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
len(x)

newlist = x[:1] + x[7:]
print newlist

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
len(x)
x1 = x[0:5]
x2 = x[5:11]
x3 = [x1] + x2
print x3