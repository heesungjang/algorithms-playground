from typing import List, Any

num_arr = [1, 2, 3, 5, 7, 9, 11, 14, 16, 19, 24, 35]


def binary_search(array: List[int], target: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return True
        elif target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1

    return False


result = binary_search(num_arr, 35)

print(result)


def binary_search_recursive(data, target):
    pass


binary_search_recursive([1, 2, 3, 5, 7, 9, 11, 14, 16, 19, 24, 35], 35)
