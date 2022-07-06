import sys
from collections import deque

input = sys.stdin.readline

t = int(input())  # 테스트 케이스 t

for _ in range(t):
    m, n, k = map(int, input().split())  # 가로길이, 세로길이, 배추가 심어진 위치 수

    field = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        y, x = x, y

        field[x][y] = 1

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]


    def bfs(y, x):
        # 1. 방문 처리
        visited[y][x] = 1
        q = deque()
        q.append((y, x))

        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if visited[ny][nx]:
                    continue

                if field[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1


    cnt = 0
    for j in range(n):
        for i in range(m):
            if field[j][i] == 1 and not visited[j][i]:
                bfs(j, i)
                cnt += 1

    print(cnt)
