graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def dfs_recursive(node, visited):
    # 방문 처리
    visited.append(node)

    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)
    return visited


print(dfs_recursive(1, []))


def dfs_stack(start):
    # store visited nodes
    visited = []

    # store nodes to be visited
    stack = [start]

    # while there are nodes to be visited continue search(visit)
    while stack:
        concurrently_visiting_node = stack.pop()
        visited.append(concurrently_visiting_node)

        # from currently visiting node
        for adj in graph[concurrently_visiting_node]:
            # if adj node have not been visited yet,
            if adj not in visited:
                # add to be visited list
                stack.append(adj)
                
    return visited


print(dfs_stack(1))
