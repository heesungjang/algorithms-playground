word = input()


def is_palin(w):
    return w == w[::-1]


print(1 if is_palin(word) else 0)
