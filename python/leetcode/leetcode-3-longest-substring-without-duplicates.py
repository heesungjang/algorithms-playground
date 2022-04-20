import collections


def length_of_longest_substring(s: str) -> int:
    seen = collections.defaultdict(int)

    # start = 0 evaluates to 0 value, thus, can be assigned to variable
    curr_max = start = 0

    for i, char in enumerate(s):
        if char in seen and start <= seen[char]:
            start = seen[char] + 1
        else:
            curr_max = max(curr_max, (i - start) + 1)
        seen[char] = i

    return curr_max


result = length_of_longest_substring("abcabcbb")

print(result)
