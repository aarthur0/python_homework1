#count
s=input("input a string ")
k=input("input the searched word ")
def countt(m,n):
    count =0
    lst=m.split()
    for i in lst:
        if(i==n):
            count+=1
    return count
    
print(countt(s,k))

