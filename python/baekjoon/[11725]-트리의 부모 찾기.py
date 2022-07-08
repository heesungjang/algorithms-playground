import collections
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().strip().split())

    graph[a].append(b)
    graph[b].append(a)


def bfs(node):
    q = collections.deque()
    q.append(node)

    while q:

        node = q.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = node
                q.append(adj)


bfs(1)

for parent in visited[2:]:
    print(parent)
