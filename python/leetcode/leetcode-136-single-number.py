import collections
from typing import List

nums = [2, 2, 1]


def single_number(nums: List[int]) -> int:
    count = collections.Counter(nums)

    for key, value in count.items():
        if value < 2:
            return key


print(single_number(nums))
