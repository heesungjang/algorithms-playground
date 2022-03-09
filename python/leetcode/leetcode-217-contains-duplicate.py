from typing import List

nums = [1, 2, 3, 1]


def contains_duplicate(nums: List[int]) -> bool:
    # nums.sort()
    #
    # for idx, _ in enumerate(nums):
    #     if nums[idx] == nums[idx + 1]:
    #         return True
    #
    # return False
    # or

    return True if len(nums) != len(set(nums)) else False


contains_duplicate(nums)
