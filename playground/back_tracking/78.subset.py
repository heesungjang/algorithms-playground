def subset(nums):
    res = []

    subset = []

    def backtracking(i):
        if i >= len(nums):
            res.append(subset[:])
            return

        # 현재 num 선택하는 decision tree
        subset.append(nums[i])
        backtracking(i + 1)

        # 현재 num 선택하지 않는 decision tree
        subset.pop()
        backtracking(i + 1)

    backtracking(0)
    return res


print(subset([1, 2, 3]))
