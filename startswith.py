#startswith
def startofstr(s,k): # s is the given string , k is the start word we want to check
	lst=s.split()
	if(k==lst[0]):
		return True
	else:
		return False
