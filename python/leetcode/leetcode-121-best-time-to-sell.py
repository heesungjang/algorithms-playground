import sys
from typing import List


def max_profit(prices: List[int]) -> int:
    # left = 0
    # right = 1
    # max_p = 0
    #
    # while right < len(prices):
    #
    #     if prices[left] > prices[right]:
    #         left = right
    #         right += 1
    #     elif prices[left] < prices[right]:
    #         max_p = max(max_p, prices[right] - prices[left])
    #         right += 1
    #
    # return max_p

    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


result = max_profit([7, 1, 5, 3, 6, 4])

print(result)
