n=int(input("enter a number:"))
original=n
sum=0
while n!=0:
    digit=n%10
    arm=digit*digit*digit
    sum+=arm
    n=n//10
if sum==original:
    print("armstrong number")
else:
    print("not an armstrong ")