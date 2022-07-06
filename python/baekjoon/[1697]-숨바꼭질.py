import collections
import sys

input = sys.stdin.readline

INT_MAX = 100001

n, k = map(int, input().split())
map = [0] * INT_MAX
visited = [0] * INT_MAX


def bfs(visited, x):
    visited[x] = 1

    q = collections.deque()
    q.append(x)

    while q:
        x = q.popleft()
        
        if x == k:
            print(visited[k] - 1)
            break
        nx = x
        for i in range(3):
            if i == 0:
                nx = x - 1
            elif i == 1:
                nx = x + 1
            elif i == 2:
                nx = x * 2

            if nx < 0 or nx >= INT_MAX:
                continue

            if visited[nx]:
                continue

            visited[nx] = visited[x] + 1
            q.append(nx)


bfs(visited, n)
