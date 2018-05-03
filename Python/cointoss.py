import random

def coin_toss():
	for i in range(0,5000):
		x = random.random()
		x_rounded = round(x)
		tails =0
		heads = 0 
		if x_rounded == 0:
			 tails += 1
			
			print "tails:", tails
		elif x_rounded == 1:
			heads += 1
			print "heads:", heads
		

coin_toss()
