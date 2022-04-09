n, x = map(int, input().split())
nums = [int(num) for num in input().split()]

result = []

for i in range(n):
    if nums[i] < x:
        result.append(str(nums[i]))

print(" ".join(result))
