import collections


def remove_duplicate(s: str) -> str:
    counter = collections.Counter(s)
    stack = []
    seen = set()

    for char in s:
        if char in seen:
            # 이미 처리된 문자, 즉 스택에서 제가할 수 없는 문자라면
            # 스택에 넣지 않고 스킵
            continue

        # 중복 문자 제거 부분
        # 현재 문자열이 스택에 있는 문자보다 알파벳 순서로 작은데,
        # 현재 스택에 있는 문자가 뒤에 더 있어서 스택에서 제거가 가능하다면
        # 모두 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return "".join(stack)


result = remove_duplicate("bcabc")

print(result)
