import collections
import sys

input = sys.stdin.readline

n = int(input())

grid = [list(input().strip()) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(color, visited, y, x):
    visited[y][x] = 1

    q = collections.deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if visited[ny][nx]:
                continue

            if grid[ny][nx] == color:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))


cnt1 = 0

for color in ["R", "G", "B"]:
    visited1 = [[0] * n for _ in range(n)]
    ret1 = 0
    for j in range(n):
        for i in range(n):
            if grid[j][i] == color and not visited1[j][i]:
                bfs(color, visited1, j, i)
                ret1 += 1
    cnt1 += ret1

for k in range(n):
    for l in range(n):
        if grid[k][l] == "G":
            grid[k][l] = "R"

cnt2 = 0
for color in ["R", "B"]:
    visited2 = [[0] * n for _ in range(n)]
    ret2 = 0
    for j in range(n):
        for i in range(n):
            if grid[j][i] == color and not visited2[j][i]:
                bfs(color, visited2, j, i)
                ret2 += 1
    cnt2 += ret2
print(cnt1, cnt2)
