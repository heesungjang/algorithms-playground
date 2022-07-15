import collections
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

MAX_INT = 100001

_map = [0] * MAX_INT
visited = [0] * MAX_INT

answer = []


def bfs():
    cnt = 0
    q = collections.deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()

        if x == k:
            cnt += 1
            continue

        nx = x
        for i in range(3):
            if i == 0:
                nx = x - 1
            elif i == 1:
                nx = x + 1
            elif i == 2:
                nx = x * 2

            if nx < 0 or nx >= MAX_INT:
                continue

            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
            else:
                if visited[nx] == visited[x] + 1:
                    q.append(nx)

    return cnt


count = bfs()
print(visited[k] - 1)
print(count)
