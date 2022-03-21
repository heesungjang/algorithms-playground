input1 = "()"
input2 = "()[]{}"
input3 = "(]"


def is_valid(s: str) -> bool:
    stack = []
    match = {"(": ")",
             "{": "}",
             "[": "]"}

    for char in s:
        if char in "({[":
            stack.append(char)
            continue
        else:
            if len(stack) == 0:
                return False

            if char == match[stack[-1]]:
                stack.pop()

            else:
                return False

    return len(stack) == 0


print(is_valid(input1))
