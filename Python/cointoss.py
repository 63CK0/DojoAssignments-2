import random

def coin_toss():
	tails =0
	heads = 0
	for i in range(0,5000):
		x = random.random()
		x_rounded = round(x) 
		if x_rounded == 0:
			tails += 1
			
			print "tails:", tails
		else:
			heads += 1
			print "heads:", heads
		

coin_toss()
