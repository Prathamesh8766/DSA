def maxprofit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return max_profit

print(maxprofit([7,1,5,3,5,6,7]))     
print(maxprofit([1]))
print(maxprofit([7,6,5,4,3,2,1]))      