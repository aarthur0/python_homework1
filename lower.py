def lower_str(s):
	k=""
	for i in s:
		if (i.isupper()):
			i=i.swapcase()
		k+=i
	return k