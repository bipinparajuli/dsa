arr=[4,2,0,1,6]
n=len(arr)
k=0
for i in range(0,n):
            if arr[i] ==0:
                print( True)
                
            for j in range(i+1,n):
                k +=arr[j]
                print(k)                
                if k ==0:
                    print(True)
                if k + arr[i] == 0:
                    print( True)
                
print( False)