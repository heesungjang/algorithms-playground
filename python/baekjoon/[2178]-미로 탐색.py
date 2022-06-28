n, m = map(int, input().split())

map = [list(map(int, list(input()))) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited[0][0] = 1

q = [(0, 0)]

while q:
    y, x = q.pop(0)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m or map[ny][nx] == 0:
            continue

        if visited[ny][nx]:
            continue

        visited[ny][nx] = visited[y][x] + 1
        q.append((ny, nx))

print(visited[n - 1][m - 1])
