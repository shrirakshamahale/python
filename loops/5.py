x=int(input("enter a number:"))
rev=0
while x !=0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
print(rev)
