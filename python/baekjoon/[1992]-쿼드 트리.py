n = int(input())  # 언제나 2의 제곱수

image = [list(map(int, list(input()))) for _ in range(n)]


def quard(y, x, size):
    if size == 1:
        return str(image[y][x])
    ret = ""
    num = image[y][x]

    for j in range(y, y + n):
        for i in range(x, x + n):
            if num != image[j][i]:
                size //= 2
                ret += "("
                ret += quard(y, x, size)
                ret += quard(y, x + size, size)
                ret += quard(y + size, x, size)
                ret += quard(y + size, x + size, size)

                ret += ")"
                return ret
    return str(image[y][x])


quard(0, 0, n)

"""
[
[1, 1, 1, 1, 0, 0, 0, 0], 
[1, 1, 1, 1, 0, 0, 0, 0], 
[0, 0, 0, 1, 1, 1, 0, 0], 
[0, 0, 0, 1, 1, 1, 0, 0], 
[1, 1, 1, 1, 0, 0, 0, 0], 
[1, 1, 1, 1, 0, 0, 0, 0], 
[1, 1, 1, 1, 0, 0, 1, 1], 
[1, 1, 1, 1, 0, 0, 1, 1]
]
"""
