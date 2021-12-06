"""
Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
"""

input = 5


def find_prime_list_under_number(number):
    prime = []

    for i in range(2, number +1):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime


result = find_prime_list_under_number(input)
print(result)
