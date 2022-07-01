n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

p = []

# 새로운 벽을 세울 수 있는 포지션 모음
for j in range(n):
    for i in range(m):
        if map[j][i] == 0:
            p.append((j, i))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(visited, y, x):
    visited[y][x] = True  # 방문 처리

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if map[ny][nx] == 1:  # 벽이라면 중지
            continue

        if map[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(visited, ny, nx)


def go():
    visited = [[False] * m for _ in range(n)]

    for j in range(n):
        for i in range(m):
            if map[j][i] == 2 and not visited[j][i]:
                dfs(visited, j, i)
    cnt = 0

    for k in range(n):
        for q in range(m):
            if not visited[k][q] and map[k][q] == 0:
                cnt += 1

    return cnt


max_size = 0
for i in range(len(p)):
    for j in range(i + 1, len(p)):
        for k in range(j + 1, len(p)):
            map[p[i][0]][p[i][1]] = 1  # 첫번째 벽
            map[p[j][0]][p[j][1]] = 1  # 두번째 벽
            map[p[k][0]][p[k][1]] = 1  # 세번째 벽

            max_size = max(max_size, go())

            map[p[i][0]][p[i][1]] = 0  # 첫번째 벽
            map[p[j][0]][p[j][1]] = 0  # 두번째 벽
            map[p[k][0]][p[k][1]] = 0  # 세번째 벽

print(max_size)
