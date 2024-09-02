def maxProfit(prices) -> int:
    profit = 0
    # start date
    buy_price = prices[0]

    # when to sell, should i keep it or sell it today
    for i in range(1, len(prices), 1):

        if buy_price < prices[i]:
            # buy day > sell day
            profit += prices[i] - buy_price
        buy_price = prices[i]

    return profit

print(maxProfit([7,1,5,3,6,4]))