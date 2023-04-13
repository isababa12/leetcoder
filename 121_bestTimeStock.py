def maxProfit(prices):

    profit = 0

    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            temp_profit = prices[sell] - prices[buy]
            if temp_profit > profit:
                profit = temp_profit

    return profit

print(maxProfit([1,2]))
