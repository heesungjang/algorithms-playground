from typing import List

array = [5, 1, 22, 25, 6, -1, 8, 10]

sequence = [1, 6, -1, 10]


def is_valid_sub_sequence(arr: List[int], seq: List[int]):
    p1 = 0
    p2 = 0

    while p1 < len(arr) and p2 < len(seq):
        if arr[p1] == seq[p2]:
            p1 += 1
            p2 += 1
        else:
            p1 += 1

    if p2 < len(seq):
        return False

    return True


print(is_valid_sub_sequence(array, sequence))
