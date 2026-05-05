"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    buy = -prices[0]
    sell = 0

    for price in prices[1:]:
        next_buy = max(buy, sell - price)
        next_sell = max(sell, buy + price)
        buy, sell = next_buy, next_sell

    return sell
