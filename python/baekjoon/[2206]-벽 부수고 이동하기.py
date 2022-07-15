import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

_map = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x, crashed):
    visited[y][x][crashed] = 1

    q = collections.deque()
    q.append((y, x, crashed))

    while q:
        y, x, crashed = q.popleft()

        if y == n - 1 and x == m - 1:
            return visited[y][x][crashed]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if visited[ny][nx][crashed]:
                continue

            if _map[ny][nx] == 0:
                q.append((ny, nx, crashed))
                visited[ny][nx][crashed] = visited[y][x][crashed] + 1
            elif _map[ny][nx] == 1:
                if crashed == 1:
                    continue
                visited[ny][nx][crashed + 1] = visited[y][x][crashed] + 1
                q.append((ny, nx, crashed + 1))

    return -1


answer = bfs(0, 0, 0)
print(answer)
