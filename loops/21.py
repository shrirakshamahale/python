n = int(input("enter a number :"))
o = int(input("enter a number:"))

for i in range(1, min(n, o) + 1):
    if n % i == 0 and o % i == 0:
        print(i)

           