#replace
def replacetheword(s,k,l):#s is the given string, k in the word we want to change with l word
	lst=s.split()
	for i in range(0,len(lst)):
		if lst[i]==k:
			lst[i]=l
	k=' '.join(lst)
	return k

	

