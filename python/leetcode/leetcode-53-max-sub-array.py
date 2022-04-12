from typing import List


def max_sub_array(nums: List[int]) -> int:
    curr_sum = max_sum = 0

    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return curr_sum


result = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)
