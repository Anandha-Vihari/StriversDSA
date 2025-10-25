n=int(input())
space=2*(n-1)
for i in range(1,n+1):
    for k in range(1,i+1,1):
        print(k,end="")
    for l in range(space):
        print(" ",end="")
    for m in range(i,0,-1):
        print(m,end="")
    space=space-2
    print()
    