arr=[[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
resultarray=[]
for i in arr:
    count=0
    for j in range(len(i)):
            if i[j]==1:
                    count +=1
    resultarray.append(count)
inde= max(resultarray)
print(resultarray.index(inde))