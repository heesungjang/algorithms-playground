def daily_temp(T):
    res, stack = [0] * len(T), []

    for i, curr in enumerate(T):

        while stack and curr > T[stack[-1]]:
            last = stack.pop()
            res[last] = i - last
        stack.append(i)

    return res


result = daily_temp([73, 74, 75, 71, 69, 72, 76, 73])
print(result)
