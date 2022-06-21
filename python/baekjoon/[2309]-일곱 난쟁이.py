from itertools import combinations

heights = [int(input()) for _ in range(9)]

sevens = combinations(heights, 7)


def find_dwarfs():
    for s in sevens:
        if sum(s) == 100:
            return s


dwarfs = sorted(find_dwarfs())

for d in dwarfs:
    print(d)
