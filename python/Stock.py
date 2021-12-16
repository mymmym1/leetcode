#121. Best Time to Buy and Sell Stock. 1 <= prices.length <= 10^5
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    profits = []
    for a in range(len(prices)):
        for b in range(len(prices)):
            if (b > a):
                dif = prices[b] - prices[a]
                profits.append(dif)
    if max(profits) > 0:
        return max(profits)
    else:
        return 0

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
print(maxProfit(prices))
