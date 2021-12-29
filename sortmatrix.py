arr=[]
output=[]
Mat=[[10,20,30,40],
[15,25,35,45], 
[27,29,37,48], 
[32,33,39,50]]
for i in Mat:
            count=len(i)
            for j in range(len(i)):
                arr.append(i[j])
arr.sort()
temp=[]
for i in arr:
            
            temp.append(i)
            if (len(temp) == count):       
                output.append(temp)
                temp=[]
print(output)