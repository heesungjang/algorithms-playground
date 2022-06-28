import sys

sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def dfs(y, x):
    res = 1
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if visited[ny][nx]:
            continue

        if grid[ny][nx] == 0:
            res += dfs(ny, nx)

    return res


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1

cnt = 0
sizes = []
for j in range(n):
    for i in range(m):
        if grid[j][i] == 0 and not visited[j][i]:
            cnt += 1
            sizes.append(dfs(j, i))

print(cnt)

for size in sorted(sizes):
    print(size, end=" ")
