n, c = map(int, input().split())

nums = list(map(int, input().split()))

counter = {}

for num in nums:

    if num not in counter:
        counter[num] = 1

    else:
        counter[num] += 1

counter = {k: v for k, v in sorted(counter.items(), key=lambda x: (-x[1], nums.index(x[0])))}

answer = []
for k, v in counter.items():
    for _ in range(v):
        answer.append(k)

print(*answer)
