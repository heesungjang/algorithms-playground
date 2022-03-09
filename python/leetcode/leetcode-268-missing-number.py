from typing import List

nums = [3, 0, 1]


def missing_number(nums: List[int]) -> int:
    nums.sort()

    if 0 not in nums:
        return 0
    for idx, _ in enumerate(nums):
        if idx == len(nums) - 1:
            return nums[idx] + 1
        if nums[idx] + 1 != nums[idx + 1]:
            return nums[idx] + 1


print(missing_number(nums))
