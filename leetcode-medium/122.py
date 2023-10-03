from typing import List


def max_profit(prices: List[int]) -> int:
    buy = float("-inf")
    sell = 0

    for price in prices:
        next_buy = max(buy, sell - price)
        next_sell = max(sell, buy + price)
        buy, sell = next_buy, next_sell  # type: ignore

    return sell
