import collections
import sys

input = sys.stdin.readline
n, m, v = map(int, input().split())

tree = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    tree[a].sort()
    tree[b].sort()


def dfs(visited, node):
    print(node, end=" ")
    visited[node] = True

    for adj in tree[node]:
        if visited[adj]:
            continue
        dfs(visited, adj)
    return


def bfs(visited, node):
    print(node, end=" ")
    visited[node] = True
    q = collections.deque()
    q.append(node)

    while q:
        node = q.popleft()

        for adj in tree[node]:
            if visited[adj]:
                continue
            print(adj, end=" ")
            visited[adj] = True
            q.append(adj)


dfs([False] * (n + 1), v)
print()
bfs([False] * (n + 1), v)
