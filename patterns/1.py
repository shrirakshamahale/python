n = int(input("Enter number of rows: "))
for i in range(n):
    print("* " * n)
"""square pattern"""


n = int(input("Enter number of rows: "))
for i in range(n):
    print("*"*i)
""" right angle"""



n=int(input("enter the number of rows:"))
for i in range(n,0,-1):
    print("*"*i)
    """inverted right angle"""


n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

