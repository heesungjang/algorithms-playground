from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    num_set = []

    def backtrack(elements):
        if len(elements) == 0:
            result.append(num_set[:])
            return

        for num in elements:
            new_list = elements[:]
            new_list.remove(num)

            num_set.append(num)
            backtrack(new_list)
            num_set.pop()

    backtrack(nums)

    return result


assert permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
