a, b, c = map(int, input().split())

time = [0] * 101

for i in range(1, 4):
    t1, t2 = map(int, input().split())
    for j in range(t1, t2):
        time[j] += 1

cost = 0

for t in time:
    if t == 1:
        cost += a
    elif t == 2:
        cost += b * 2
    elif t == 3:
        cost += c * 3

print(cost)
