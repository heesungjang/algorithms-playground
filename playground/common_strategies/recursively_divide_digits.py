"""
재귀를 이용하면 숫자에서 각 자릿수의 값을 가지고 원하는 연산을 할 수 있다.

예시) 숫자 1527에서 각 자리 숫자의 합은 1 + 5 + 2 + 7 = 15이다.

숫자 1527의 각 자리 숫자의 합은 숫자 152의 각 자리 숫자의 합에 끝 숫자인 7을 더한 값이다.

즉,
f(1527) = f(152) + 7 이고,
f(152)  = f(15)  + 2 이고,
f(15)   = f(1)   + 5 이다.

아래 코드로 살펴보자.
"""


def recursively_add_digits(n: int) -> int:
    # n이 10보다 작다면 즉, 마지막 1의 자릿수라면,
    if n < 10:
        return n

    return recursively_add_digits(n // 10) + n % 10


assert recursively_add_digits(1527) == 15


# 같은 방법을 응용하면 각 자리 숫자의 제곱 합을 출력할 수 있다.
def recursively_add_squared_digits(n: int) -> int:
    # n이 10보다 작다면, 즉, 마지막 1의 자릿수라면 제곱을 리턴
    if n < 10:
        return n * n

    return recursively_add_squared_digits(n // 10) + (n % 10) * (n % 10)


# 654321 = (6*6) + (5*5) + (4*4) + (3*3) + (2*2) + (1*1) == 91
assert recursively_add_squared_digits(654321) == 91
