n = int(input())

pattern = input().split("*")

names = [input() for _ in range(n)]

for name in names:
    start = pattern[0]
    end = pattern[-1]

    if name[0:len(start)] == start and name[len(name) - len(end):] == end and len(name) > len(start + end):
        print("DA")
    else:
        print("NE")
