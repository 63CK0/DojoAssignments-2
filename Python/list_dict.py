name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def list_dict(lst1,lst2):
	join_lst = zip(lst1,lst2)
	lst_dict = dict(join_lst)

	print lst_dict

list_dict(name,favorite_animal)