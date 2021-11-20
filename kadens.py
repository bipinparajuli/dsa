
def maxsum(arr):
    sum=0
    max_sum=0

    for i in arr:

        sum +=i
        print(sum,max_sum)
        if sum>max_sum:
            max_sum=sum
        
        if sum<0:
            sum=0
    
    return max_sum

print(maxsum([5,-4,-2,6,-1]))