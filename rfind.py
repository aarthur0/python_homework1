#rfind
def findtheword(s,k):# s is the given string , k is the  word we want to find
	for i in range(len(s.split())-1,-1,-1):
		if(s.split()[i]==k):
			return len(s)-1-len(s.split()[i])-1
