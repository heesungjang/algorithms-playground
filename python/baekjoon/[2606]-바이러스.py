import sys

input = sys.stdin.readline

n = int(input())  # 컴퓨터의 수
v = int(input())

computers = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(v):
    a, b = map(int, input().split())

    computers[a].append(b)
    computers[b].append(a)


def dfs(visited, node):
    cnt = 0
    visited[node] = True

    for adj in computers[node]:
        if visited[adj]:
            continue

        cnt += dfs(visited, adj) + 1

    return cnt


answer = dfs(visited, 1)

print(answer)
