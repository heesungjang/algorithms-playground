from typing import List


def array_pair_sum(nums: List[int]) -> int:
    # [1,2,2,5,6,6]
    print(sorted(nums)[::2])
    # nums.sort()
    # max_sum = 0
    # pair = []
    #
    # for num in nums:
    #     pair.append(num)
    #
    #     if len(pair) == 2:
    #         max_sum += min(pair)
    #         pair = []
    #
    # return max_sum


result = array_pair_sum([6, 2, 6, 5, 1, 2])
print(result)
