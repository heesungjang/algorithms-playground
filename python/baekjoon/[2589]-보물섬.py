"""
1. 각 유지마다 bfs를 돌고, 최장 거리를 저장함
2. visited 초기화하고 다음 위치에서 BFS를 돌면서 최장 거리르 저장함
"""
import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

_map = [list(input().strip()) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(visited, y, x):
    visited[y][x] = 1
    _max = -sys.maxsize
    q = collections.deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if visited[ny][nx] or _map[ny][nx] == "W":
                continue

            if _map[ny][nx] == "L":
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
                _max = max(_max, visited[ny][nx])

    return _max


answer = -sys.maxsize
for j in range(n):
    for i in range(m):
        visited = [[0] * m for _ in range(n)]
        if _map[j][i] == "L":
            answer = max(answer, bfs(visited, j, i))

print(answer - 1)
