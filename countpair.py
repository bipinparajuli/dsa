arr=[1,5,7,1]
n=len(arr)
k=6
c=0
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]+arr[j] == k:
            c = c + 1
print(c)