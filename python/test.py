def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1: right]


def longest_palindrome(s: str):
    # 1. s가 길이가 2보다 작거나 즉, a 처럼 싱글 문자 이거나 또는
    # 2. 입렵 문자열 자체가 palindrome 일 때
    # 입력 문자열 그대로 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    # 가장긴 palindrome 을 저장
    result = ""
    # 마지막 문자는 어차피 palindrome 이 아니기 때문에 len() - 1 까지만 반복
    for i in range(len(s) - 1):
        # 각 인덱스 위치에서 찾은 palindrome중 길이를 key 가장 큰 값을 result 에 저장
        result = max(result,
                     expand(s, i, i + 1),  # even 일 경우
                     expand(s, i, i + 2),  # odd 일 경우
                     key=len)

    return result


odd = longest_palindrome("babad")
print(odd)
even = longest_palindrome("cbbd")
print(even)
