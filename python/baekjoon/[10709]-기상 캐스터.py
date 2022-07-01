n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
map = [list(map(lambda x: x.replace(".", "0"), list(input()))) for _ in range(n)]


def bfs(y, x):
    visited[y][x] = 1

    q = [(y, x)]

    while q:
        y, x = q.pop(0)

        ny, nx = y, x + 1
        if nx >= m or visited[ny][nx] or map[ny][nx] == "c":
            continue

        if map[ny][nx] == "0":
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))


for j in range(n):
    for i in range(m):

        # 구름을 이라면
        if map[j][i] == "c" and not visited[j][i]:
            bfs(j, i)

for k in range(n):
    for q in range(m):
        print(visited[k][q] - 1, end=" ")

    print()
