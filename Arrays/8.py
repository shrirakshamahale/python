n = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter element to search: "))

index = -1

for i in range(len(n)):
    if n[i] == target:
        index = i
        break

print(index)
