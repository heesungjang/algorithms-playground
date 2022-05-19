from typing import List


def max_profit(prices: List[int]):
    left, right = 0, 1  # 투 포인터 위치
    max_p = 0  # 가장 큰 수익 추적

    while right < len(prices):
        # left(사는 지점)이 right(파는 지점)보다 작다면 == 수익 발생
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]  # 현재 수익
            max_p = max(max_p, profit)  # 가장 큰 수익 추적
        else:
            # ! 여기서 "left pointer" 를 +1 증가해 줄 수도 있지만,
            # else문에 걸렸다면 right 값이 left보다 작은것이고 가장 큰 수익을 내기 위해서 left는 가장 작은 값이 팔요하기 때문에
            # left를 right 위치로 이동시켜준다.
            left = right
        right += 1
    print(max_p)
    return max_p


assert max_profit([7, 1, 5, 3, 6, 4]) == 5

assert max_profit([7, 6, 4, 3, 1]) == 0
