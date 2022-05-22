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
    # n이 10보다 작다면 즉, 분할해서 최종적으로 한자리 수가 재귀 호출에 들어갔을때
    if n < 10:
        return n

    return recursively_add_digits(n // 10) + n % 10


assert recursively_add_digits(1527) == 15


# 같은 방법을 응용하면 각 자리 숫자의 제곱 합을 출력할 수 있다.
def recursively_add_squared_digits(n: int) -> int:
    # n이 10보다 작다면 즉, 숫자를 분할해서 최종적으로 한자리 수가 재귀 호출에 들어갔을때
    if n < 10:
        return n * n

    return recursively_add_squared_digits(n // 10) + (n % 10) * (n % 10)


# 654321 = (6*6) + (5*5) + (4*4) + (3*3) + (2*2) + (1*1) == 91
assert recursively_add_squared_digits(654321) == 91


# 조금 더 응용해서 이번에는 짝수를 제외한 합을 구해보자.
def recursively_add_odd_digits(n: int) -> int:
    # 마지막 한자리 수의 값이 짝수라면 0을 리턴
    if n < 10:
        if n % 10 == 0:
            return 0
        else:
            return n

    last_digit = n % 10

    if last_digit % 2 == 0:  # 짝수라면
        return recursively_add_odd_digits(n // 10)
    else:
        return recursively_add_odd_digits(n // 10) + last_digit


assert recursively_add_odd_digits(1527) == 13
