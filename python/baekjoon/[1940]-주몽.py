import itertools

n = int(input())  # 재료의 개수

m = int(input())  # 갑옷을 만드는데 필요한 수

nums = list(map(int, input().split()))

num_set = {}

for num in nums:
    pair = m - num

    if pair in num_set:
        num_set[pair] += 1
    else:
        num_set[num] = 1

cnt = 0

for v in num_set.values():
    if v > 1:
        cnt += 1

print(cnt)
