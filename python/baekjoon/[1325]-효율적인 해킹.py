import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n = 컴퓨터 수, m = 신뢰 줄

tree = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())  # e.g) 5, 4
    tree[b].append(a)


def bfs(visited, node):
    visited[node] = True
    ret = 1

    queue = collections.deque()
    queue.append(node)

    while queue:
        x = queue.popleft()

        for adj in tree[x]:
            if not visited[adj]:
                visited[adj] = True
                ret += 1
                queue.append(adj)
    return ret


_max = 0
answer = []
for j in range(len(tree)):
    visited = [False] * (n + 1)
    cnt = bfs(visited, j)
    if cnt > _max:
        _max = cnt
        answer = [j]
    elif cnt == _max:
        answer.append(j)

print(answer)
