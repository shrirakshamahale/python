n = list(map(int, input("Enter numbers: ").split()))

is_sorted = True

for i in range(len(n) - 1):
    if n[i] > n[i + 1]:
        is_sorted = False
        break

print(is_sorted)
