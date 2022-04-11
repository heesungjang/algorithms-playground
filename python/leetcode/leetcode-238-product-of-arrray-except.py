import collections
from typing import List


def product_except_self(nums: List[int]):
    products = [1 for _ in range(len(nums))]
    prefix = [1 for _ in range(len(nums))]
    suffix = [1 for _ in range(len(nums))]

    curr_prefix_products = 1
    for i in range(len(prefix)):
        prefix[i] = curr_prefix_products
        curr_prefix_products *= nums[i]

    curr_suffix_products = 1
    for i in reversed(range(len(suffix))):
        suffix[i] = curr_suffix_products
        curr_suffix_products *= nums[i]

    for i in range(len(products)):
        products[i] = prefix[i] * suffix[i]

    return products


result = product_except_self([1, 2, 3, 4])
print(result)
