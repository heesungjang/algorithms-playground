"""
겹치는 구간이나 지점을 구하는 문제는 어떻게 접근하는게 좋을까?

A가 [2, 5] 구간을, B가 [3, 8] 구간을 청소했다고 하자,

총 몇 개의 칸을 청소 했을까?

2개의 구간이 주어진 경우이므로 다음과 같이 2가지로 나눠서 생각해 볼 수 있다

Case 1. 두 구간이 겹치는 경우
예) A : [2, 5], B : [3, 8]

Case 2. 두 구간이 겹치지 않는 경우
예) A : [2, 5], B : [10, 15]

하지만 이렇게 케이스를 나눠서 계산하는 방식이 아니라 1차원 배열을 하나 만들어,
직접 시물레이션을 진행하는 방법으로 해결이 가능하다.
"""

# 청소 구간이 0 - 10 이라고 가정하고, 0으로 초기화한 1차원 배열을 만들어준다.
cleaned = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# A가 청소한 구간인 [2,5]를 반복문으로 순회하며 방문 처리를 한다.
cleaned = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# 또, B가 청소한 구간은 [3, 8]이라 했으므로, 이번에는 3에서 8까지의 값을 전부 1로 바꿔준다.
cleaned = [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]
# 최종적으로 전체 구간을 쭉 순회하며 1인 곳의 개수를 세면 청소를 진행한 칸의 갯수를 구할 수 있다.

"""
그렇다면 특정 칸이나 지역이 아닌, 겹치는 구간은 어떻게 접근하는게 좋을까?

예시) [2, 5]와 [4, 8] 사이에 겹치는 지점은 총 몇 곳 있을까?

[1] [1] [1] [2] [2] [0] [0] [0]
            [2] [2] [1] [1] [1] [1] [1]
            
2로 표시된 구간이 두 선분이 겹치는 구간이다. 여기서 2를 카운트해서 출력하면 2개의 구간이 겹친다는 답을 얻게된다.
하지만 실제 겹치는 구간은 4에서 시작해서 5에서 끝나는 한 곳의 구간이다. 

올바른 구간을 출력하기 위해서는 반복문으로 방문하는 범위를 X1부터 X2-1까지만 표기해줘야 한다.
"""

OFFSET = 100  # 최소 값이 -100이기 때문에, 가장 작은 값에서 100을 더해주면 양수
MAX_SPACE = 200  # -100 ~ 100
n = int(input())

ranges = [list(map(int, input().split())) for _ in range(n)]

check = [0] * 202
for x1, x2 in ranges:
    for i in range(x1, x2):  # x1 ~ x2 -1 까지
        x1, x2 = x1 + OFFSET, x2 + OFFSET
        check[i] += 1

print(max(check))

"""
예시) 왔다 갔던 구역 구하기

문제: 치 0에서 시작하여 n번의 명령에 걸쳐 움직인 뒤, 2번 이상 지나간 영역의 크기를 출력하는 프로그램을 작성해라. 
단 명령은 “x L“, “x R” 형태로만 주어집니다. "x L" 의 경우 왼쪽으로 x만큼 이동해야 함을, 
"x R"의 경우 오른쪽으로 x만큼 이동해야 함을 뜻한다.
"""
n = int(input())

operations = [list(input().split()) for _ in range(n)]

curr_idx = 0
map = {}

for num, direction in operations:
    num = int(num)
    if direction == "R":
        for j in range(0, num):
            if (curr_idx + j) in map:
                map[curr_idx + j] += 1
            else:
                map[curr_idx + j] = 1
        curr_idx += num

    if direction == "L":
        for j in range(1, num + 1):
            if (curr_idx - j) in map:
                map[curr_idx - j] += 1
            else:
                map[curr_idx - j] = 1
        curr_idx -= num

cnt = 0

for i, j in map.items():
    if j >= 2:
        cnt += 1

print(cnt)
