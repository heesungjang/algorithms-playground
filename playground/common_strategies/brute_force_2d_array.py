"""
2차원 배열로 만들어진 격자들이 등장하는 문제들을 익혀보자.

5 * 5 크기의 격자 정보가 아래와 같을때,

1 0 0 0 0
0 1 0 0 0
0 1 1 0 1
0 0 0 1 0
0 0 0 0 0


각 칸에 동전이 있다면 1, 없다면 0이 적혀있다.
5 * 5 격자를 벗어나지 않도록 1 * 2 크기의 격자를 적절하게 잘 잡아서,
해당 범위 안에 들어있는 동전의 개수를 최대로 했을 때,
얻을 수 있는 동전의 개수는 몇 개일까??

1 0 0 0 0
0 1 0 0 0
0 [1 1] 0 1 <-- 2개의 크기를 담는 배열을 만들어 완젙 탐색을 구할 수 있다.
0 0 0 1 0
0 0 0 0 0
"""

import sys


def get_best_adj_sum(n, arr):
    max_sum = -sys.maxsize

    for i in range(n):
        for j in range(n - 1):
            max_sum = max(max_sum, (arr[i][j] + arr[i][j + 1]))

    return max_sum


assert get_best_adj_sum(
    5,
    [[1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 1, 0, 1],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0]]) == 2

"""
* 격자 위에서의 가장 좋은 위치 (응용 문제)


N * N 크기의 격자 정보가 주어진다.
이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어진다.
N * N 격자를 벗어나지 않도록 1 * 3 크기의 격자를 적절하게 잘 잡아서, 
해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성하자.
"""

n = 3
arr = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]
max_sum = -sys.maxsize
for i in range(n):
    for j in range(n - 2):
        max_sum = max(max_sum, arr[i][j] + arr[i][j + 1] + arr[i][j + 2])

print(max_sum)  # 2
