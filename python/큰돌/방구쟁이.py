"""
1 0 1 0 1
1 1 0 0 1
0 0 0 1 1
0 0 0 1 1
0 1 0 0 0
"""

n, m = map(int, input().split())

island = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

cnt = 0


def dfs(y, x):
    island[y][x] = 0  # 방문 처리
    for i in range(4):  # 동서남북 탐색
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if island[ny][nx] == 1:
            dfs(ny, nx)
    return


for i in range(n):
    for j in range(m):

        if island[i][j] == 1:  # 방문하지 않은 섬이라면
            dfs(i, j)  # dfs 탐색
            cnt += 1
print(cnt)
