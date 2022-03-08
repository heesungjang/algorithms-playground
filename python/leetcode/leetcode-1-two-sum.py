from typing import List

nums = [2, 7, 11, 15]
target = 9


def two_sum(nums: List[int], target: int) -> List[int]:
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


print(two_sum(nums, target))
