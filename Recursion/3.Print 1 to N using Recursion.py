def oneton(N,curr=1):
    if curr>N:
        return
    print(curr)
    oneton(N,curr+1)

oneton(10)