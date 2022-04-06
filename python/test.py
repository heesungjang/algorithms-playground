from typing import List


def two_sum_pointer(array: List[int], target: int) -> List[int]:
    left = 0
    right = len(array) - 1
    # data = [3, 5, -4, 8, 11, 1, -1, 6]
    # [-4, -1, 1, 3, 5, 6, 8 ,11]
    #  p                       p
    # o(n log n)
    # o(1)


def two_sum_hash(array: List[int], target: int) -> List[int]:
    map = {}
    # O(n)
    # [3, 5, -4, 8, 11, 1, -1, 6]
    for num in array:
        # 10 - 3 = 7
        match = target - num
        # O(n)
        # set . dictionary  O(1)
        if match in map:
            return [match, num]
        else:
            map[num] = True
    return []


def two_sum_for(array, target):
    # O(n)
    for i in range(len(array) - 1):
        first = array[i]
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return [1, 2]


if __name__ == "__main__":
    data = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    result1 = two_sum_pointer(data, target_sum)
    print(result1)

    data = [3, 5, -4, 8, 11, 1, -1, 6]
    result2 = two_sum_hash(data, target_sum)
    print(result2)

    data = [3, 5, -4, 8, 11, 1, -1, 6]
    result3 = two_sum_for(data, target_sum)
    print(result3)
