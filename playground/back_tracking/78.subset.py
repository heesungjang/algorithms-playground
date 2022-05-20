def subset(nums):
    res = []

    subset = []

    def backtracking(i):
        if i >= len(nums):
            res.append(subset[:])
            return

        subset.append(nums[i])
        backtracking(i + 1)

        subset.pop()
        backtracking(i + 1)

    backtracking(0)
    return res


print(subset([1, 2, 3]))
