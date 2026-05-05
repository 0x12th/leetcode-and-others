"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
"""


def max_profit(prices: list[int]) -> int:
    max_profit = 0
    buy = prices[0]
    for next_price in prices[1:]:
        if next_price > buy:
            max_profit = max(max_profit, next_price - buy)
        else:
            buy = next_price
    return max_profit
