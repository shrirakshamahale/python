n=list(map(int,input("enter the list of numbers :").split()))
count=0
for i in range(0,len(n)):
    if n[i]%2!=0:
        count+=1
print(count)