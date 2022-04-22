from typing import List

g = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


# def num_island(grid: List[List[str]]) -> int:
#     # 상하좌우 탐색 좌표가 필요함
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     count = 0
#
#     rows, columns = len(grid), len(grid[0])
#
#     for row in range(rows):
#         for column in range(columns):
#
#             if grid[row][column] != "1":
#                 continue
#
#             count += 1
#             stack = [(row, column)]
#
#             while stack:
#                 x, y = stack.pop()
#                 # 방문 처리
#                 grid[x][y] = "0"
#
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#
#                     if nx < 0 or nx >= rows or ny < 0 or ny >= columns or grid[nx][ny] != "1":
#                         continue
#
#                     stack.append((nx, ny))
#
#     return count


def num_island(grid: List[List[str]]) -> int:
    def dfs(x, y):
        # 종료 조건
        if x < 0 or x >= rows or y < 0 or y >= columns or grid[x][y] != "1":
            return

        # 방문 처리
        grid[x][y] = "0"

        # 동 서 남 북 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    # 섬의 갯수
    count = 0

    # 행열 생성
    rows, columns = len(grid), len(grid[0])
    for row in range(rows):
        for column in range(columns):
            # 방문한 노드가 섬이 아니면 다음 노드로 이동
            if grid[row][column] != "1":
                continue

            # 방문한 노드가 섬이면 dfs 탐색 시작
            dfs(row, column)

            # dfs 탐색이 끝나면 섬 카운트 1 증가
            count += 1

    return count


assert num_island([["1", "1", "1", "1", "0"],
                   ["1", "1", "0", "1", "0"],
                   ["1", "1", "0", "0", "0"],
                   ["0", "0", "0", "0", "0"]]) == 1

assert num_island([["1", "1", "0", "0", "0"],
                   ["1", "1", "0", "1", "0"],
                   ["0", "0", "1", "0", "0"],
                   ["0", "1", "0", "1", "1"]]) == 5
