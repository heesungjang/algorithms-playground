def letter_combination(digits):
    def dfs(i, cur_str):
        # 종료 조건
        # letters 조합은 digits 길이와 같을 때 까지만 탐색하면 된다.
        if len(cur_str) == len(digits):
            result.append(cur_str)
            return
        chars = dic[digits[i]]
        for char in chars:
            dfs(i + 1, cur_str + char)

    if not digits:
        return []

    result = []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    # 0번 인덱스는 digit에 첫번째 letter로 맵핑된다.
    # dfs 탐색 시작
    dfs(0, "")
    # dfs 탐색 종료
    print(result)
    return result


assert letter_combination("2345") == ["a", "b", "c"]
