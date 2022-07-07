import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(node):
    visited[node] = 1

    q = collections.deque()
    q.append(node)

    while q:

        node = q.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = visited[node] + 1
                q.append(adj)


cnt = 0
for i in range(1, n + 1):
    # print(graph)
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
