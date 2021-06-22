def AA(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def BB(a, b):
    return a * b // AA(a, b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(BB(a, b))
