import collections

chars = list(input())

chars.sort(reverse=True)
counter = {}

for c in chars:
    if c not in counter:
        counter[c] = 1
    else:
        counter[c] += 1


def cnt_odds():
    cnt = 0
    for key, value in counter.items():
        if value % 2 != 0:
            cnt += 1

    return cnt


def is_palin():
    if cnt_odds() > 1:
        return "I'm Sorry Hansoo"
    else:
        palindrome = collections.deque()

        for key, value in counter.items():
            if value % 2 != 0:
                palindrome.append(key)
                counter[key] -= 1

        for key, value in counter.items():
            if value > 0:
                for _ in range(value // 2):
                    palindrome.appendleft(key)
                    palindrome.append(key)

        return "".join(list(palindrome))


answer = is_palin()

print(answer)
