import string

word = list(input())


def cnt_chars(word: list) -> list:
    alphas = list(string.ascii_lowercase)

    for i in range(len(alphas)):
        alphas[i] = word.count(alphas[i])

    return alphas


cnt = cnt_chars(word)

for c in cnt:
    print(c, end=" ")
