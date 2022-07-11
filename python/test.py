n = int(input())


def recur_add(n):
    if n == 1:
        return 1

    return n + recur_add(n - 1)


answer = recur_add(n)
print(answer)


def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


answer1 = fibo(10)
print(answer1)
