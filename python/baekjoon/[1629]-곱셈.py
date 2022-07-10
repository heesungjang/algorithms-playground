a, b, c = map(int, input().split())


def recur(a, b):
    if b == 1:
        return a % c

    _c = recur(a, b // 2)

    _c = (_c * _c) % c

    if b % 2 == 1:
        _c = (_c * a) % c
    return _c


answer = recur(a, b)

print(answer)
