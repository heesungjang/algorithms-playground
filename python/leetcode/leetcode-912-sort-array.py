from typing import List


def sort_array_selection(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n):
        curr_min = i
        for j in range(i, n):
            if nums[j] < nums[curr_min]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


result1 = sort_array_selection([3, 1, 2])
result2 = sort_array_selection([5, 1, 1, 2, 0, 0])

print(result1)
print(result2)


def sort_array_bubble(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


result3 = sort_array_bubble([5, 1, 1, 2, 0, 0])
print(result3)


def merge(left: List[int], right: List[int]):
    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)

    return merged


def merge_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    if n <= 1:
        return nums
    else:
        mid = n // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])

        return merge(left, right)


result4 = merge_sort([5, 1, 1, 2, 0, 0])
print(result4)
