import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    stack = []
    ps = input().strip()
    flag = True
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                flag = False
                break
            if stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
    if flag and not stack:
        print("YES")
    else:
        print("NO")