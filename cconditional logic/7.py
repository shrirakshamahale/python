x,y=map(int,input("enter two numbers : ").split())
result=(x+y+abs(x-y))//2
print("the largest number is :",result)

x,y,z=map(int,input("enter three numbers :").split())
max_val=x
if y>max_val:max_val=y
if z>max_val:max_val=z
print("the max val is :",max_val)


n=int(input("enter a number:"))
if n<0:n=-n
print("the absolute value is ",n)


x=str(input("enter two strings"))
y=str(input("enter two strings"))
for i in range(len(x+1)):
    if x[i]==y[i]:
        print("the strings are equal")
    else:
        print("the strings are not equal")
