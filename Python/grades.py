import random

def grades():
	
	for i in range(0,10):
		random_grade = random.randint(60,100)
		if random_grade < 70:
			print "Score:", random_grade,"Your grade is D"
		if 70 <= random_grade < 80:
			print "Score:", random_grade,"Your grade is C"
		if 80 <= random_grade < 90:
			print "Score:", random_grade,"Your grade is B"
		if 90 <= random_grade <= 100:
			print "Score:", random_grade,"Your grade is A"
grades()



