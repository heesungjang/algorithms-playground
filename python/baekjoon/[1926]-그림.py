"""
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

cnt = 0  # 그림의 수
max_size = 0
visited = [[False] * m for _ in range(n)]


# def dfs(y, x):
#     global size
#     size += 1
#     map[y][x] = 0
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if ny < 0 or ny >= n or nx < 0 or nx >= m:
#             continue
#         else:
#             if map[ny][nx] == 1:
#                 dfs(ny, nx)
#     return


def bfs(y, x):
    rs = 1
    visited[y][x] = True
    q = [(y, x)]
    while q:
        ey, ex = q.pop()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
                continue
            if map[ny][nx] == 1 and not visited[ny][nx]:
                rs += 1
                visited[ny][nx] = True
                q.append((ny, nx))
    return rs


for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and not visited[j][i]:
            cnt += 1
            max_size = max(max_size, bfs(j, i))

print(cnt, max_size)
