import itertools
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

mutals = [0] * 3

for i, v in enumerate(list(map(int, input().split()))):
    mutals[i] = v

hits = list(itertools.permutations([9, 3, 1], 3))


def bfs(visited, y, x, z):
    q = deque()
    q.append((y, x, z))
    visited[y][x][z] = 1

    while q:
        y, x, z = q.popleft()

        for i in range(6):
            ny = max(0, y - hits[i][0])
            nx = max(0, x - hits[i][1])
            nz = max(0, z - hits[i][2])

            if visited[ny][nx][nz]:
                continue
            visited[ny][nx][nz] = visited[y][x][z] + 1
            q.append((ny, nx, nz))


y, x, z = mutals

visited = [[[0] * 61 for _ in range(61)] for _ in range(61)]

bfs(visited, y, x, z)

print(visited[0][0][0] - 1)
