# get fibonacci value:

def fib(n: int) -> int:
    # 피보나치 수열에서 1, 2번 원소는 이전 두 요소가 없기 때문에 1로 정의.
    # e.g) 1 1 2 3 5
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(3))
