x = int(input())
print(2 ** x - 1)


def hanoi(n, p1, p2, p3):
    if n == 1:
        print(p1, p3)
    else:
        hanoi(n - 1, p1, p3, p2)
        print(p1, p3)
        hanoi(n - 1, p2, p1, p3)


hanoi(x, 1, 2, 3)
