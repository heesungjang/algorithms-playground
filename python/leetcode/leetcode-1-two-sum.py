import collections
from typing import List

nums = [2, 7, 11, 15]
target = 9


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """Given an array of integers nums and an integer target,
      return indices of the two numbers such that they add up to target.

      Example:

      Input: nums = [2,7,11,15], target = 9
      Output: [0,1]
      """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


two_sum_brute_force(nums, target)


def two_sum_in(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        potential_pair = target - num
        if potential_pair in nums[i + 1:]:
            return [i, nums[i + 1:].index(potential_pair) + (i + 1)]


two_sum_in(nums, target)


def two_sum_map(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


two_sum_map(nums, target)


# def two_sum_pointer(nums: List[int], target: int) -> List[int]:
#     original_list = nums[:]
#     nums.sort()
#
#     left = 0
#     right = len(nums) - 1
#
#     while left < right:
#         if nums[left] + nums[right] == target:
#             return [original_list.index(nums[left]), original_list.index(nums[right])]
#         elif nums[left] + nums[right] < target:
#             left += 1
#             continue
#         elif nums[left] + nums[right] > target:
#             right -= 1
#             continue

def two_sum_pointer(nums: List[int], target: int) -> List[int]:
    original_list = nums[:]
    nums.sort()

    left = 0
    right = len(nums) - 1

    index_1 = 0
    index_2 = 0

    ans = []
    while left < right:
        if nums[left] + nums[right] == target:
            index_1 = nums[left]
            index_2 = nums[right]
            break
        elif nums[left] + nums[right] < target:
            left += 1
            continue
        elif nums[left] + nums[right] > target:
            right -= 1
            continue

    for i in range(len(nums)):
        if original_list[i] == index_1:
            ans.append(i)
        elif original_list[i] == index_2:
            ans.append(i)

    return ans


print(two_sum_pointer(nums, target))
