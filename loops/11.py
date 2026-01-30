n=list(map(int,input("enter the numbers:").split()))
smallest=n[0]
for i in range(1,len(n)):
    if n[i]<smallest:
        smallest=n[i]
print(smallest)
