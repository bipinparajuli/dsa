matrix = [
           [1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]
k=0 #starting row index
l=0 #starting column index
m=len(matrix) #ending index of row
n=len(matrix[0])# ending column index

while k<m and l<n:
    #fist row
    for i in range(l,n):
        print(matrix[k][i],end="")
    k +=1

    # print last colum from remaing col
    for i in range(k,m):
        print(matrix[i][n-1],end="")            
    n -=1


    #print last row from remaining row
    if k<m:

        for i in range(n - 1, l-1, - 1):
            print(matrix[m-1][i],end="")
        m -=1
    #print first column from remaing column
    if l<n:
        for i in range(m-1,k-1,-1):
            print(matrix[i][l],end="")

        l +=1
    