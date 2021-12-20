price=[7,1,5,3,6,4]
# price=[7,6,4,3,1]
c=0
for i in range(len(price)-1):
    if price[i] > price[i+1]:
        c = c+1
        continue
if len(price)-1 == c:
    print(0)
else:
    buy=price[0]
    sell=0
    result=0
    for i in price:
        if(i<buy):
            buy=i
            x=price.index(buy)
    for i in range(x+1,len(price)-1):
        if sell < price[i]:
            sell=price[i]
    result=sell-buy
    print(result)