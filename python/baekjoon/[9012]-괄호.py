n = int(input())

for _ in range(n):
    PS = input()

    if PS[0] == ")":
        print("NO")
        continue

    stack = []

    for s in PS:
        if s == "(":
            stack.append(s)
        else:
            if stack and stack[0] == "(":
                stack.pop()
            else:
                stack.append(s)

    print("NO" if stack else "YES")
