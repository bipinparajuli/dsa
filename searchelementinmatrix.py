matrix = [[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]]
target = 0

for i in matrix:
    # print(i)
    # if target > i[len(i)-1]:
        # continue
    for j in range(len(i)):
        if target > i[len(i)-1]:
            continue
        if i[j] == target:
            print(i[j])
        