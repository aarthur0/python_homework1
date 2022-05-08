#count
s=input("input a string ")
k=input("input the searched word ")
count =0
lst=s.split()
for i in lst:
    if(i==k):
        count+=1
print(count)
