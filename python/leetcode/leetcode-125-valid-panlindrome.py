import collections
from typing import Deque

s = "A man, a plan, a canal: Panama"


# Using pointer approach
def is_palindrome(s: str) -> bool:
    target_str = []

    for char in s:
        # if character is not alphabet or number
        if char.isalnum():
            target_str.append(char.lower())

    left_pointer = 0
    right_pointer = len(target_str) - 1

    while left_pointer < right_pointer:
        if target_str[left_pointer] != target_str[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True


is_palindrome(s)


# Using Deque
def is_palindrome_with_deque(string: str) -> bool:
    target_strs: Deque = collections.deque()

    for char in string:
        if char.isalnum():
            target_strs.append(char.lower())

    while len(target_strs) > 1:
        if target_strs.popleft() != target_strs.pop():
            return False

    return True


is_palindrome_with_deque(s)
