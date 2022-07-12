import collections
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(visited, y, x):
    q = collections.deque()
    temp = []
    visited[y][x] = True

    q.append((y, x))
    temp.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if visited[ny][nx]:
                continue

            diff = abs(_map[ny][nx] - _map[y][x])

            if l <= diff <= r:
                visited[ny][nx] = True
                temp.append((ny, nx))
                q.append((ny, nx))

    return temp


answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = 1
    for j in range(n):
        for i in range(n):
            if not visited[j][i]:
                moved = bfs(visited, j, i)
                if len(moved) > 1:
                    flag = 0
                    new_num = sum([_map[y][x] for y, x in moved]) // len(moved)
                    for x, y in moved:
                        _map[x][y] = new_num

    if flag:
        break
    answer += 1

print(answer)
