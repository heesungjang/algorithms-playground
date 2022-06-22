n = int(input())

cnt = 0
for _ in range(n):
    stack = []
    chars = list(input())
    for c in chars:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

    if not stack:
        cnt += 1

print(cnt)
