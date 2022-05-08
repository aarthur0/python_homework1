#strip
def stripspaces(s):
	lst=s.split()
	for i in range(0,len(lst)):
		while lst[i]==" ":
			del(lst[i])
	for i in range(len(lst)-1,-1,-1):
		while lst[i]==" ":
			del(lst[i])
	k=' '.join(lst)
	return k


	
