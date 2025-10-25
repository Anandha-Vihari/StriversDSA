n = int(input())
spaces = 0

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(spaces):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    spaces += 2
    print()

spaces = 2 * (n-1)
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    for j in range(spaces):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    spaces -= 2
    print()
