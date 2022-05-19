from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    1. dfs backtracking why?
        - because we don't know the k
        - thus, can not work out with nested for loop
    2. when does recursion end?
        - when len(nums) == k
    3. for 돌면서 dfs

    """
    result = []

    def backtrack(elements, start, k):
        if k == 0:
            result.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            backtrack(elements, start + 1, k - 1)
            elements.pop()

    backtrack([], 1, k)
    print(result)
    return result


assert combine(3, 3) == [[1]]

# assert combine(4, 2) == [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
