import collections


def remove_duplicate(s: str) -> str:
    counter, stack, seen = collections.Counter(s), [], set()

    for char in s:
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return "".join(stack)


result = remove_duplicate("bcabc")

print(result)
