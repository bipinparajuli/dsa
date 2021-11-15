arr =[-12, 11, -13, -5, 6, -7, 5, -3, -6]

temp=[]
p=[]
for i in arr:
    if(i<0):
        temp.append(i)
    else:
        p.append(i)
temp.extend(p)
print(temp)