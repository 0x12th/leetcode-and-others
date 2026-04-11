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
