from typing import List, Any

num_arr = [1, 2, 3, 5, 7, 9, 11, 14, 16, 19, 24, 35]


def binary_search(array: List[int], key: Any) -> int:
    pl = 0
    pr = len(array) - 1
    while True:
        pc = (pl + pr) // 2
        if array[pc] == key:
            return pc
        elif array[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1


print(binary_search(num_arr, 35))
