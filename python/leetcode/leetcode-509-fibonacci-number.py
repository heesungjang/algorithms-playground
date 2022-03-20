# before memorization
def non_memo_fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a positive integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return non_memo_fib(n - 1) + non_memo_fib(n - 2)


print(non_memo_fib(3))


def memo_fib(n: int, memorization=None) -> int:
    if memorization is None:
        memorization = {0: 0, 1: 1}

    if n in memorization:
        return memorization[n]
    else:
        memorization[n] = memo_fib(n - 1, memorization) + memo_fib(n - 2, memorization)
        return memorization[n]


print(memo_fib(3))


def liter_fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    
    last_two = [0, 1]
    counter = 2

    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


print(liter_fib(3))
