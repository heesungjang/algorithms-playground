def longest_palindrome(s: str) -> str:
    res = ""

    for i in range(len(s)):
        # odd
        temp = get_longest_palindrome(s, i, i)
        if len(temp) > len(res):
            res = temp

        temp = get_longest_palindrome(s, i, i + 1)
        if len(temp) > len(res):
            res = temp
    return res


def get_longest_palindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]


print(longest_palindrome("cbbd"))
