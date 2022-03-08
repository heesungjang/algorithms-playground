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


print(two_sum_in(nums, target))
