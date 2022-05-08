#endswith
def endofstr(s,k):# s is the given string , k is the end word we want to check
	lst=s.split()
	if(k==lst[-1]):
		return True
	else:
		return False
