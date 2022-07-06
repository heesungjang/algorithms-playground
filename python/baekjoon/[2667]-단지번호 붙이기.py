import sys

input = sys.stdin.readline

n = int(input())

map = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(visited, y, x):
    ret = 1
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if visited[ny][nx]:
            continue

        if map[ny][nx] == 1:
            ret += dfs(visited, ny, nx)

    return ret


cnt = 0
result = []
for j in range(n):
    for i in range(n):

        if map[j][i] == 1 and not visited[j][i]:
            cnt += 1
            result.append(dfs(visited, j, i))

result.sort()

print(cnt)
for r in result:
    print(r)
