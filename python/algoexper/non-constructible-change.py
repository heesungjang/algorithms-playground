from typing import List

list = [5, 7, 1, 1, 2, 3, 22]


def non_constructible(coins: List[int]) -> int:
    # sort the list of coins
    # O(log n) time complexity
    # [1, 1, 2, 3, 5, 7, 22]

    curr_constructible_coin = 0

    for coin in sorted(coins):
        if coin > curr_constructible_coin + 1:
            return curr_constructible_coin + 1

        curr_constructible_coin += coin

    return curr_constructible_coin + 1


print(non_constructible(list))
