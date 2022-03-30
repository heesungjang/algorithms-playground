g = [
    [],
    [2, 3, 4],
    [5],
    [5],
    [],
    [6, 7],
    [],
    [3],
]


def bfs_recursive(graph, node, visited=[]):
    # 첫번째 노드 vertex 처리
    visited.append(node)

    for adj in graph[node]:
        if adj not in visited:
            bfs_recursive(graph, adj, visited)

    return visited


def bfs_stack(graph, start):
    visited = []

    stack = [start]

    while stack:
        top = stack.pop()
        visited.append(top)
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited


print(bfs_recursive(g, 1))
print(bfs_stack(g, 1))
