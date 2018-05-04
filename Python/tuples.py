my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def make_tuple(dict):
	lst = []
	for key, value in dict.iteritems():
		lst.append((key,value))
	print lst
make_tuple(my_dict)