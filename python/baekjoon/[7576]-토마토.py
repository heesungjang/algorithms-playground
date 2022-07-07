import collections
import sys

input = sys.stdin.readline

m, n = map(int, input().strip().split())

field = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

q = collections.deque()


def dfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m or field[ny][nx] == -1:
                continue

            if field[ny][nx] == 0 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1


for j in range(n):
    for i in range(m):
        if field[j][i] == 1 and not visited[j][i]:
            q.append((j, i))
            visited[j][i] = 1

dfs()

answer = -sys.maxsize

for j in range(n):
    answer = max(answer, max(visited[j]))
    for i in range(m):
        if visited[j][i] == 0 and field[j][i] == 0:
            print(-1)
            sys.exit(0)

print(answer - 1)
