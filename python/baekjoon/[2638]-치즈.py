import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]


def dfs(visited, y, x):
    cnt = 0
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
            continue

        if map[ny][nx] == 1:
            cnt += 1
            map[ny][nx] = 0
            visited[ny][nx] = True
        elif map[ny][nx] == 0:
            visited[ny][nx] = True
            cnt += dfs(visited, ny, nx)

    return cnt


time = 0
cheeses = []
while True:
    time += 1
    visited = [[False] * m for _ in range(n)]
    cnt = dfs(visited, 0, 0)
    if cnt == 0:
        break
    cheeses.append(cnt)

print(time - 1)  # 마지막 while문에서는 없는 치즈를 확인했기 때문에 그 1시간전에 치즈는 다 사라짐
print(cheeses[-1])
