from typing import List

g = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


def num_island(grid: List[List[str]]) -> int:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    count = 0

    rows, columns = len(grid), len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] != "1":
                continue

            count += 1
            stack = [(row, column)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = "0"


assert num_island([["1", "1", "1", "1", "0"],
                   ["1", "1", "0", "1", "0"],
                   ["1", "1", "0", "0", "0"],
                   ["0", "0", "0", "0", "0"]]) == 1

assert num_island([["1", "1", "0", "0", "0"],
                   ["1", "1", "0", "1", "0"],
                   ["0", "0", "1", "0", "0"],
                   ["0", "1", "0", "1", "1"]]) == 5
