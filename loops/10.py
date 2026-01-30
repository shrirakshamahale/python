n = list(map(int, input("Enter numbers: ").split()))

largest = n[0]

for i in range(1, len(n)):
    if n[i] > largest:
        largest = n[i]

print("Largest number:", largest)
