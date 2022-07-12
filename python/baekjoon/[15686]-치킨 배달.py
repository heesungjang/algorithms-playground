import sys

input = sys.stdin.readline

"""
1. m개의 치킨집을 고른다.
2. 각 집을 돌면서, 치킨 거리를 찾는다
- 치킨 거리 계산 식:
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
여러곳의 치킨집이 있다면 최소 거리가 치킨 거리이다.

3. 도시 치킨 거리는 각 집의 치킨 거리의 합.
4. 최소 도시 치킨 거리를 찾는다.
치킨집 거리 계산 식: 
"""

n, m = map(int, input().strip().split())

city = [list(map(int, input().split())) for _ in range(n)]  # 도시 지도

homes = []
chicks = []
selected_chicks = []  # m개의 치킨집 조합


def combi(start, ls):
    if len(ls) == m:  # 조합이 완성되면 selected_chicks에 담고 recur 종료
        selected_chicks.append(ls[::-1])
        return

    for i in range(start, len(chicks)):
        ls.append(chicks[i])
        combi(i + 1, ls)
        ls.pop()

    return


for j in range(n):
    for i in range(n):
        if city[j][i] == 2:
            chicks.append((j, i))
        elif city[j][i] == 1:
            homes.append((j, i))

combi(0, [])

answer = sys.maxsize
for sc in selected_chicks:
    ret = 0
    for h in homes:
        y1, x1 = h
        min_dist = sys.maxsize
        for c in sc:
            y2, x2 = c
            min_dist = min(min_dist, abs(x1 - x2) + abs(y1 - y2))

        ret += min_dist

    answer = min(answer, ret)

print(answer)
