from collections import Counter
from typing import List

nums = [4, 3, 2, 7, 8, 2, 3, 1]


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    disappeared_list = []

    mapped_nums = Counter(nums)

    for i in range(1, len(nums) + 1):
        if i not in mapped_nums:
            disappeared_list.append(i)

    return disappeared_list


print(find_disappeared_numbers(nums))
