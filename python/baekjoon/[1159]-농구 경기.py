n = int(input())

names = [input() for _ in range(n)]

names = set(sorted(names))
names_map = {}

for name in names:
    f_char = name[0]

    if f_char not in names_map:
        names_map[f_char] = 1
    else:
        names_map[f_char] += 1

if max(names_map.values()) < 5:
    print("PREDAJA")
else:
    for key, value in sorted(names_map.items()):
        if value >= 5:
            print(key, end="")
