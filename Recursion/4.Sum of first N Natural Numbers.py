def sumofn(N,curr=1):
    if curr>N:
        return 0
    return curr+sumofn(N,curr+1)
    
print(sumofn(10))