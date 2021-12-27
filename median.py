import math
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]
l=[]
for i in M:
    for j in range(len(i)):
        l.append(i[j])
l.sort()
a=math.floor(len(l)/2)
print(l[a])