n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            new_sum = nums[i] + nums[j] + nums[k]
            if new_sum <= m:
                if new_sum == 500:
                    print(nums[i], nums[j], nums[k])
                max_sum = max(max_sum, new_sum)

print(max_sum)
