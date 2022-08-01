input = [1, 2, 3, 4]


def contains_duplicate(nums):
    nums.sort()

    flag = False

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            flag = True

    return True if flag else False


print(contains_duplicate(input))
