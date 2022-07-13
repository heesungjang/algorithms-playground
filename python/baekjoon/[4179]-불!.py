import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

_map = [list(input().strip()) for _ in range(n)]

fire = deque()
jihoon = deque()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for j in range(n):
    for i in range(m):
        if _map[j][i] == "J":
            jihoon.append((j, i))
        elif _map[j][i] == "F":
            fire.append((j, i))

f_visited = [[0] * m for _ in range(n)]

while fire:
    y, x = fire.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if _map[ny][nx] == "#":
            continue

        if f_visited[ny][nx]:
            continue

        if _map[ny][nx] == ".":
            f_visited[ny][nx] = f_visited[y][x] + 1
            fire.append((ny, nx))

j_visited = [[0] * m for _ in range(n)]
flag = 0
while jihoon:

    y, x = jihoon.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            print(j_visited[y][x] + 1)
            flag = 1
            break

        if _map[ny][nx] == "#":
            continue

        if j_visited[ny][nx]:
            continue

        if f_visited[ny][nx] and j_visited[y][x] + 1 >= f_visited[ny][nx]:
            continue

        if _map[ny][nx] == ".":
            j_visited[ny][nx] = j_visited[y][x] + 1
            jihoon.append((ny, nx))
    if flag:
        break

if not flag:
    print("IMPOSSIBLE")

"""
2 2
JF
FF
"""
