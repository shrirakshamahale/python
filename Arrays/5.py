n=list(map(int, input("enter the number :").split()))
count=0
for i in range(len(n)):
    if n[i]>0:
        count+=1
        print("positive number :",count)
    if n[i]<0:
        count+=1
        print("negtive number :",count)
    if n[i]==0:
       count+=1
       print("zero number",count)