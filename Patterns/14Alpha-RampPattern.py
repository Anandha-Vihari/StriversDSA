n=int(input())
for i in range(1,n+1):
    for j in range(0,i-1):
        print(chr(65+i-2),end="")
    print()