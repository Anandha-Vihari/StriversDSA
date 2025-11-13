def noto1(num):
    if num<=0:
        return
    print(num)
    noto1(num-1)

noto1(10)