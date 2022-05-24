# 2진법으로 표현하기
from typing import List


def get_binary_of(n: int):
    digits = []

    while True:
        if n < 2:
            digits.append(n)
            break

        digits.append(n % 2)
        n //= 2

    return int("".join(list(map(str, digits[::-1]))))


# 2진법으로 표현하기 (재귀)
digits = []


def get_binary_of_by_recursion(n: int):
    if n == 1:
        digits.append(n)
        return 1

    digits.append(n % 2)
    return get_binary_of_by_recursion(n // 2)


assert get_binary_of(29) == 11101
get_binary_of_by_recursion(29)
print("".join(list(map(str, digits[::-1]))))


# 반대로 십진수를 이진수를 바꿔보자

def binary_to_decimal(n):
    n = list(str(n))
    decimal_num = 0
    for i in range(len(n)):
        decimal_num = decimal_num * 2 + int(n[i])

    return decimal_num


assert binary_to_decimal(11101) == 29


# 십진수를 이진수로 바꿔 곱을하고 다시 십진수로 출력해보자.

def binary_to_decimal_and_back(n: int):
    n = list(map(int, list(str(n))))
    decimal = 0

    for i in range(len(n)):
        decimal = decimal * 2 + n[i]

    decimal *= 17
    digits = []
    while True:
        if decimal == 1:
            digits.append(decimal)
            break

        digits.append(decimal % 2)
        decimal //= 2

    return int("".join(list(map(str, digits[::-1]))))


assert binary_to_decimal_and_back(10011) == 101000011
