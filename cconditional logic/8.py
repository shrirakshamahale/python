x = input("enter a chacter")
y = input("enter a chacter")

for i in range(len(x)):
    if x[i] != y[i]:
        print("Not equal")
        break
else:
    print("Equal")
