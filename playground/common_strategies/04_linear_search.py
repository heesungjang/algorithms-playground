from typing import List


def linear_search(l: List[int], value: int) -> int:
    i = 0
    while True:
        if i == len(l):
            return False
        if l[i] == value:
            return i
        i += 1


lst = [2, 3, 4, 5, 6, 8, 9, 10]

result = linear_search(lst, 5)

if result:
    print(f"the value is at idx position: {result}")
else:
    print("Failed searching")
