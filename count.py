#count
def coount(m,n): # m is the given string , n is the word we want to count
    count =0
    lst=m.split()
    for i in lst:
        if(i==n):
            count+=1
    return count

