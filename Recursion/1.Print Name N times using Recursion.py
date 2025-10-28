def ntimes(name,count):
    if count==0:
        return
    print(name)
    ntimes(name,count-1)
    

ntimes("anandha",10)