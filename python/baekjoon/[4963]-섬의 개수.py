import collections
import sys

input = sys.stdin.readline

dy = [1, 0, -1, 0, 1, -1, 1, -1]
dx = [0, 1, 0, -1, 1, -1, -1, 1]


def bfs(visited, y, x):
    q = collections.deque()
    visited[y][x] = 1

    q.append((y, x))
    
    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if visited[ny][nx]:
                continue

            if lands[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))


while True:
    m, n = map(int, input().strip().split())
    if m == 0 and n == 0:
        sys.exit(0)

    if m == 1 and n == 1:
        land = int(input())
        if land == 0:
            print(0)
            continue
        else:
            print(1)
            continue

    else:
        lands = [list(map(int, input().strip().split())) for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        cnt = 0
        for j in range(n):
            for i in range(m):
                if lands[j][i] == 1 and not visited[j][i]:
                    bfs(visited, j, i)
                    cnt += 1
        print(cnt)
