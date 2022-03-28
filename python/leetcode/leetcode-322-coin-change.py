from pprint import pprint
from typing import List


## 그리디 접근 실패

def coin_change(coins: List[int], amount: int) -> int:
    coins.sort(key=lambda x: x, reverse=True)

    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count


coin_change([186, 419, 83, 408], 6249)


def coin_change_dp(coins: List[int], amount: int) -> int:
    # 0부터 amount까지 포함하는 배열 초기화
    dp = [float("inf") for amount in range(amount + 1)]

    # 0원의 만들기 위해서 필요한 코인은 0개
    dp[0] = 0

    for coin in coins:
        for amount in range(len(dp)):
            if coin <= amount:
                # if amount = 186
                # dp[amount] = 186  --> dp[186] --> 1
                # min(infinity, dp[186 - coin(186) --> 0 +1 = 1]
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


coin_change_dp([186, 419, 83, 408], 6249)
