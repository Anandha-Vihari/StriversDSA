"""n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



n=int(input())
for i in range(1,n+1):
    print(*range(1,i+1))"""


n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()