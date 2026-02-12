n=list(map(int,input("enter the number :").split()))
count=0
for i in range(len(n)):
    if n[i]%2==0:
        count+=1
print(count)
if n[i]%2!=0:
    count+=1
print(count)