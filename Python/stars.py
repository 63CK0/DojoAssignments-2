
def stars(lst):
	for x in lst:
		if isinstance(x, int or float):
			print '*'*x
		if isinstance(x, str):
			length = len(x)
			letter = x[0].upper()
			print letter * length

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)