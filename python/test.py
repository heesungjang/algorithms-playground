"""
char set: a b c


a b c a b c b b
l
r
"""


def longest_substring_without_duplicate(s: str) -> int:
    seen = {}

    longest = cur_len = cur_start = 0

    for i, char in enumerate(s):
        if char in seen and seen[char] >= cur_start:  # seen character should only apply to current window
            cur_start = seen[char] + 1
            cur_len = i - seen[char]
            seen[char] = i
        else:
            seen[char] = i
            cur_len += 1
            longest = max(cur_len, longest)

    return longest


assert longest_substring_without_duplicate("abcabcbb")
