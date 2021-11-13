arr=[9,2,3,4,55,1,22]

max=arr[0]
min=arr[0]

for i in arr:
    if(i<min):
        min=i
    
    if(i>max):
        max=i

print(min,max)
        