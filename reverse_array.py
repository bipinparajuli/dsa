arr = [2,3,4,5]
temp=[]
x=len(arr)
for i in arr:
    temp.insert(x,i)
    x-=x
print(temp)