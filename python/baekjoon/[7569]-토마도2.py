import collections
import sys

input = sys.stdin.readline

m, n, h = map(int, input().strip().split())

grid = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = collections.deque()

for z in range(h):
    for j in range(n):
        for i in range(m):
            if grid[z][j][i] == 1:
                q.append((z, j, i))

dy = [1, 0, -1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m or nz < 0 or nz >= h:
                continue

            if grid[nz][ny][nx] == 0:
                grid[nz][ny][nx] = grid[z][y][x] + 1
                q.append((nz, ny, nx))


bfs()

flag = 0
answer = -sys.maxsize

for z in range(h):
    for y in range(n):
        for x in range(m):
            if grid[z][y][x] == 0:
                flag = 1

            answer = max(answer, grid[z][y][x])

if flag:
    print(-1)
else:
    print(answer - 1)
"""
[

[
[1, 1, 1, 1], 
[1, 1, 1, 1], 
[1, 1, 1, 1]
], 

[

[1, 1, 1, 1], 
[-1, -1, -1, -1], 
[1, 1, 1, -1]
]

]

"""
