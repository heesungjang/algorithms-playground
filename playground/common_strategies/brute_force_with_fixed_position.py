"""
완전 탐색을 연산이 오래 걸리는 무식한 방법으로 생각할 때가 있다.

하지만 무식해 보여도 사실은 최고의 방법일 때가 있다.

코딩 테스트에서 가능한 모든 상황을 조해서 문제를 풀어야하는 완점 탐색 문제를 유형별로 풀어보고 정복해보자.
"""

"""
* 한 자리를 정하여 진행하는 완전 탐색

5개의 숫자 [1, 5, 2, 6, 8]이 주어졌을 때
이 중 단 하나의 숫자만 두 배로 해서, 인접한 숫자간의 차이의 합이 최대가 되도록 해보자.


이 문제는 단순하게, 모든 위치의 숫자를 2배씩 해보는 완전탐색을 진행해 볼 수 있다.
"""

import sys

n = 5

arr = [1, 5, 2, 6, 8]

INT_MIN = -sys.maxsize


def get_max_diff(n, arr):
    max_diff = INT_MIN  # 초기 최대 값을 가능한 최소 값으로 설정

    for i in range(n):  # outer for loop 에서 모든 요소를 순회
        # i 위치에 2를 곱했을 때 인접한 숫자간의 차이의 합을 저장
        sum_diff = 0
        arr[i] = arr[i] * 2

        # i가 2배인 상태에서 배열 내부에 인접한 숫자간의 차이를 구함
        for j in range(n - 1):
            sum_diff += abs(arr[j + 1] - arr[j])

        max_diff = max(sum_diff, max_diff)  # 차이의 합중 최대 값을 추적
        arr[i] //= 2  # 다음 i에 2를 곱하기 이전에 현재 i를 원래 상태로 되돌림

    return max_diff


assert get_max_diff(n, arr) == 23

"""
* 한 자리를 정하여 진행하는 완전 탐색 (응용 문제)

n개의 집이 x = 1에서 x = n까지 순서대로 놓여있고, 각각 A 명의 사람이 살고 있다. 

이들은 회의를 위해 n개의 집 중 한 곳에 전부 모이려고 한다. 

적절한 집을 선택하여 모든 사람의 이동 거리의 합이 최소가 되는 집을 찾아라.

1번째 집으로 모이면 총 이동 거리의 합은 
1x0 + 2x1 + 3x2 + 2x3 + 6x4 = 38
"""


def find_house_for_min_dist(n, arr):
    max_sum = sys.maxsize  # 최소 합을 찾기 때문에 초기 값을 sys의 최대 값으로 설정

    for i in range(n):
        sum_dist = 0  # i의 집을 모이는 장소로 선택했을 때 모든 사람의 이동 거리의 합을 저장

        # 모이는 장소로 선택된 i의 위치로부터 이동해야 하는 사람들의 합을 구함
        for j in range(n):
            sum_dist += abs(j - i) * arr[j]

        max_sum = min(max_sum, sum_dist)  # 가장 작은 합을 추적

    return max_sum


assert find_house_for_min_dist(5, [1, 2, 3, 2, 6]) == 16

"""
* 두 자리를 정하여 완전탐색

4개의 숫자 [1, 5, 2, 6]이 주어졌을 때
이 중 서로 다른 2개의 숫자만 두 배로 해서, 인접한 숫자간의 차이의 합이 최대가 되도록 해보자.

"""


def get_max_diff_2(n, arr):
    max_sum = -sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            arr[i], arr[j] = arr[i] * 2, arr[j] * 2
            sum_diff = 0
            for k in range(n - 1):
                sum_diff += abs(arr[k + 1] - arr[k])

            max_sum = max(max_sum, sum_diff)
            arr[i], arr[j] = arr[i] // 2, arr[j] // 2

    return max_sum
