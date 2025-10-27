def armstrong(n):
    nlen=len(str(n))
    nn=n
    m=0
    while n>0:
        ld=n%10
        m+=ld**nlen
        n=n//10
    if nn==m:
        return "Yes"
    else:
        return "No"
    
print(armstrong(234567654))