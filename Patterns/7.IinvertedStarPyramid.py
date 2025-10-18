n=int(input())
for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-(2*i+1)):
        print("*",end="")
    for l in range(i):
        print(" ",end="")
    print()
