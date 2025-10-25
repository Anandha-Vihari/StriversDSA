n=int(input())
space=2*n-2
for i in range(1,2*n):
    star=i
    if i>n:
        star=2*n-i
    for j in range(1,star+1):
        print("*",end="")
    for k in range(1,space+1):
        print(" ",end="")
    for l in range(1,star+1):
        print("*",end="")
    print()
    if i<n:
        space-=2
    else:
        space+=2