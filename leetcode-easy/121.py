from typing import List


def max_profit(prices: List[int]) -> int:
    max_profit = 0
    buy = prices[0]
    for next_price in prices[1:]:
        if next_price > buy:
            max_profit = max(max_profit, next_price - buy)
        else:
            buy = next_price
    return max_profit
