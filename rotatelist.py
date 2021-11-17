arr=[1,2,3,4,5]
m=arr[len(arr)-1]
temp=[]
    
for i in range(0,len(arr)-1):
    temp.append(arr[i])
    
temp.insert(0,m)
print(temp)