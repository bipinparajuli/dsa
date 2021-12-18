nums = [1,5,8,4,7,6,5,3,1]
large = nums[0]
c=False
for i in range(1,len(nums)):
    if large>nums[i]:
        if nums[i] == nums[-1]:
            c=True
        continue
    else:
        break
if(c):
    nums.sort()
    print(nums)
# res = int("".join(map(str, nums)))
# for()          158476531
                # 158576431
                # 158513467
else:
    x=len(nums)-1
    newlist=[]
    while x>=0:
        if nums[x]<nums[x-1]:
            newlist.append(nums[x])
            x=x-1
            continue
        else:
            j=nums[x-1]
            newlist.append(nums[x])
            print(j,newlist)
            # break
            for i in newlist:
            # break
                if j<i:
                    # nums.insert(x-1,i)
                    swapindex= nums.index(i,x)
                    nums[x-1],nums[swapindex] = nums[swapindex],nums[x-1] 
                    print(nums)
                    break
                else:
                    print(i)
                    continue
            break        
