n, m = map(int, input().split())

nums = list(map(int, input().split()))

p_sum = [0] * (n + 1)

for i in range(n):
    p_sum[i + 1] = p_sum[i] + nums[i]

for _ in range(m):
    a, b = map(int, input().split())

    print(p_sum[b] - p_sum[a - 1])
