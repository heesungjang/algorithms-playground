from typing import List

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def numIslands(grid: List[List[str]]) -> int:
    # count

    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                count += 1

    return count


def dfs(grid, r, c):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
        return

    grid[r][c] = '0'

    # dfs(grid, r + 1, c)
    # dfs(grid, r + -1, c)
    # dfs(grid, r, c + 1)
    # dfs(grid, r, c - 1)
    
    for i in range(4):
        dfs(grid, r + dy[i], c + dx[i])
    return


print(numIslands(grid))
