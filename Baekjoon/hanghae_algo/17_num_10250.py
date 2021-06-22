T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    dist = N // H + 1
    floor = N % H
    if floor == 0:
        dist -= 1
        floor = H
    print(floor * 100 + dist)
