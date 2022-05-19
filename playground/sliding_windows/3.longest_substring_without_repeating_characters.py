def longest_substring(s: str) -> int:
    # 왜 딕셔너리를 사용했을까요?
    # 브루트포스로 이 문제를 푼다고 생각하면 O(n^3)겠죠?
    # 모든 인덱스 위치에서 2중 포문으로 탐색을 하니까 n^2에
    # 현재 관찰중인 substring 내에서 중복된 문자가 있는지 또 반복문을 돌면서 확인하겠죠? == n
    # n^2 * n == n^3

    sub = {}  # 딕셔너리에 저장하면 상수 시간에 중복 문자 탐색이 가능 합니다.
    curr_start = 0
    curr_len = 0
    longest = 0

    for i, letter in enumerate(s):
        if letter in sub and sub[letter] >= curr_start:
            curr_start = sub[letter] + 1
            curr_len = i - sub[letter]
            sub[letter] = i

        else:
            sub[letter] = i
            curr_len += 1
            longest = max(curr_len, longest)

    return longest


assert longest_substring("abcabcbb") == 3
