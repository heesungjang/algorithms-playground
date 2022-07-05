import sys

n = int(input())

graph = list(map(int, input().split()))

remove = int(input())

adj = [[] for _ in range(n)]


def dfs(node):
    child = 0
    ret = 0

    for j in range(len(adj[node])):
        if adj[node][j] == remove:
            continue

        ret += dfs(adj[node][j])
        child += 1

    if child == 0:
        return 1

    return ret


def go():
    root = 0

    for i in range(n):
        if graph[i] == -1:
            root = i
        else:
            adj[graph[i]].append(i)

    if remove == root:
        print(0)
        sys.exit(0)

    cnt = dfs(root)
    print(cnt)


go()
