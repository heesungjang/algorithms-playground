map = [[0] * 100 for _ in range(100)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

"""
[ x x x x
y[0 0 0 0]
y[0 0 0 0]
y[0 0 0 0]
]
"""
# for i in range(len(map)):
#     for j in range(len(map)):
#         if i == 1 and j == 1:
#             for k in range(4):
#                 ny = i + dy[k]
#                 nx = i + dx[k]
#                 print(ny, nx)

for y in range(len(map)):
    for x in range(len(map)):
        if y == 0 and x == 0:
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny < 0 or ny >= len(map) or nx < 0 or nx >= len(map):
                    continue
                print(ny, nx)
