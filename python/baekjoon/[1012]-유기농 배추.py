import sys

sys.setrecursionlimit(10000)

t = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x):
    field[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if field[ny][nx] == 1:
            dfs(ny, nx)
    return


for _ in range(t):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]

    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for j in range(n):
        for i in range(m):
            if field[j][i] == 1:
                cnt += 1
                dfs(j, i)

    print(cnt)
