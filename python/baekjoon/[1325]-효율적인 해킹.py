import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[b].append(a)


def bfs(visited, node):
    ret = 0
    visited[node] = 1

    q = collections.deque()
    q.append(node)

    while q:
        node = q.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                ret += 1
                visited[adj] = visited[node] + 1
                q.append(adj)
    return ret


cnts = []
max_cnt = -sys.maxsize
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    cnt = bfs(visited, i)
    cnts.append(cnt)
    max_cnt = max(max_cnt, cnt)

answer = []

for i, c in enumerate(cnts):
    if c == max_cnt:
        answer.append(i + 1)
answer.sort()

for a in answer:
    print(a, end=" ")
