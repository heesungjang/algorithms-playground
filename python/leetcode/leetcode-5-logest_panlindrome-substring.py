# def get_longest_palindrome_from(str, start, end):
#     while start >= 0 and end < len(str):
#         if str[start] != str[end]:
#             break
#         start -= 1
#         end += 1
#
#     return [start + 1, end]
#
#
# def longest_palindrome_substring(strs: str) -> str:
#     # string[0:1] = this will be used as slicing indexes.
#     current_longest = [0, 1]
#
#     for i in range(1, len(strs)):
#         odd_center = get_longest_palindrome_from(strs, i - 1, i + 1)
#         even_center = get_longest_palindrome_from(strs, i - 1, i)
#         logest = max(odd_center, even_center, key=lambda x: x[1] - x[0])
#         current_longest = max(logest, current_longest, key=lambda x: x[1] - x[0])
#
#     return strs[current_longest[0]: current_longest[1]]
#
#
strs = "abb"


#
# print(longest_palindrome_substring(strs))


def find_longest_palindrome(string, left, right):
    if right == len(string) - 1 and string[right - 1] == string[right]:
        return string[right - 1:right + 1]

    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return string[left + 1:right]


def longest_palindrome(strs: str) -> str:
    # if strs length is less than 2, it is palindrome
    # if reversed strs is equal to strs, it is the longest palindrome
    if len(strs) < 2 or strs == strs[::-1]:
        return strs

    # initial longest is the first single character in string
    current_longest = strs[0:1]

    # iterate through strings and find the longest palindrome
    for i in range(1, len(strs) - 1):
        even_longest = find_longest_palindrome(strs, i - 1, i + 1)
        odd_longest = find_longest_palindrome(strs, i - 1, i)
        longest = max(even_longest, odd_longest, key=len)
        current_longest = max(longest, current_longest, key=len)

    return current_longest


print(longest_palindrome(strs))
