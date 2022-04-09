from typing import List


def reverse_string(s: List[int]) -> List[int]:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


result = reverse_string(["h", "e", "l", "l", "o"])
print(result)
