from collections import Counter
arr = [1,2,3,4,5,6,1,1,1]
count = Counter(arr)
low,high=min(count.values()),max(count.values())
min_ele=[]
max_ele=[]
for i,j in count.items():
    if j==low:
        min_ele.append(i)
    if j==high:
        max_ele.append(i)

print(min_ele,max_ele)