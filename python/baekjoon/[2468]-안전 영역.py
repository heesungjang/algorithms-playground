import sys

sys.setrecursionlimit(100000)

n = int(input())

geo = [list(map(int, input().split())) for _ in range(n)]

MAX = max((map(max, geo)))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 0

visited = [[False] * n for _ in range(n)]


def dfs(y, x, h):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx]:
            continue

        if geo[ny][nx] <= h:
            continue

        if geo[ny][nx] > h:
            dfs(ny, nx, h)
    return


for h in range(MAX + 1):
    cnt = 0
    for j in range(n):
        for i in range(n):
            if geo[j][i] > h and not visited[j][i]:
                dfs(j, i, h)
                cnt += 1
    answer = max(answer, cnt)
    visited = [[False] * n for _ in range(n)]

print(answer)
