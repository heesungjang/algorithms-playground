def longest_substring(s: str) -> int:
    """
    브루트포스로 이 문제를 푼다고 생각하면 O(n^3)
    모든 인덱스 위치에서 2중 포문으로 탐색을 하니까 n^2
    현재 substring 내에서 중복된 문자 확인 n
    """

    sub = {}
    curr_start = 0
    curr_len = 0
    longest = 0

    for i, letter in enumerate(s):
        if letter in sub and sub[letter] >= curr_start:  # 윈도우 내에서 중복 발생
            curr_start = sub[letter] + 1  # 문자 시작점 오른쪽으로 한 칸 이동
            curr_len = i - sub[letter]  # 윈도우 내 문자열 길이 갱신
            sub[letter] = i  # 방문 처리

        else:
            sub[letter] = i  # 방문 처리
            curr_len += 1
            longest = max(curr_len, longest)

    return longest


assert longest_substring("abcabcbb") == 3
