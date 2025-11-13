def revarr(arr,n):
    ans=[0]*n
    for i in range(n-1,-1,-1):
        ans[n-i-1]=arr[i]
    print(ans)

arr=(1,2,3,4,5)
revarr(arr,5)