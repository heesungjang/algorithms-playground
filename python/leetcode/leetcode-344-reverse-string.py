from typing import List

s = ["h", "e", "l", "l", "o"]


def reverse_string(s: List[str]) -> None:
    left_pointer, right_pointer = 0, len(s) - 1

    while left_pointer < right_pointer:
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1


def reverse_string_pythonic(s: List[str]) -> None:
    s.reverse()
