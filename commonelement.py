A = {3,3,3,3,3}
B = {3,3,3,3,3}
C = {3,3,3,3,3}
temp=[]
for i in A:
    for j in B:
        for k in C:
                if(i == j == k):
                    if temp.count(i)==0:
                        temp.append(i)
print(temp)
