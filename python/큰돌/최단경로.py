n, m = map(int, input().split())

sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, 1]

visited = [[0] * m for _ in range(n)]

visited[sy][sx] = 1
q = [(sy, sx)]

while q:
    y, x = q.pop()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
            continue
        if map[ny][nx] == 1:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

"""
[
[1, 0, 5, 0, 9], 
[2, 3, 4, 0, 8], 
[0, 0, 5, 6, 7], 
[0, 0, 6, 7, 8], 
[0, 0, 7, 8, 9]

5 5
0 0
4 4
1 0 1 0 1
1 1 1 0 1
0 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

print(visited[ey][ex])
