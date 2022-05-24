"""
수열을 구하는 문제는 재귀를 사용하면 간결한 코트가 간결해진다.


아래처럼 점화식이 주어지고 해당 점화식을 만족하는 수열에서 n번째 값을 구하는 문제가 있다고 하자,

A1 = 2, A2 = 7, 그리고 An = An-1 + 2 * An-2

수열 문제는 보통 A1과 A2와 같이 첫번째 위치의 값과 두번째 위치 값과 같이 초기 값들이 주어진다.

이러한 초기 값들은 종료 조건에 대한 정보를 준다.

위 점화식을 만족하는 재귀 코드를 작성하면 아래와 같다.
"""


def f(n):
    # 종료 조건
    if n == 1:
        return 2
    if n == 2:
        return 7

    # 점화식
    return f(n - 1) + 2 * f(n - 2)


assert f(4) == 25


# 피보나치 수열: 대표적인 수열 문제
# 재귀 접근 방식을 위한 코드이기 때문에 dp를 활용한 최적화 x
# 피보나치 수열에서 첫 번째와 두 번째 요소는 1이고
# 세 번째 원소부터는 value = n-1 + n-2 이다.
def fib(n):
    if n <= 2:  # 초기 값으로 주어진 종료 조건
        return 1

    return fib(n - 1) + fib(n - 2)  # 점화식


assert fib(3) == 2


# 조금 더 복잡한 점화식의 수열이 주어져도 위에서 활용한 접근법을 적용하면 쉽게 재귀 코드를 작성할 수 있다

# 자연수 n이 주어지고.
# n에서 시작하여 n이 짝수면 2로 나누고,
# n이 홀수면 3을 곱하고 1을 더하는 것을 n이 1이 되기 전까지 계속 반복한다.
# 총 몇 번을 반복해야 1이 되는가?

def little_more_complex_sequence(n):
    if n == 1:  # n이 1이 되기까지 실행하기 때문에
        return 0  # n이 1이면 1을 만들기 위해서 0번의 연산이 필요함

    if n % 2 == 0:
        return little_more_complex_sequence(n // 2) + 1
    else:
        return little_more_complex_sequence(n * 3 + 1) + 1


assert little_more_complex_sequence(3) == 7


# 같은 방법으로 또 다른 수열 문제를 풀어보자.

# 첫  번째는 4,번째는 2, 두
# 세 번째부터는 앞의 두 수의 곱을 100으로 나눈 나머지로 이루어진 수열이 있다.
# 100 이하의 정수 N을 입력받아 재귀함수를 이용하여 N번째 값을 구하여 출력해보자.

def another_complex_sequence(n):
    # 마찬가지로 초기 값으로 주어진 정보들로 베이스 케이스를 작성한다.
    if n == 1:
        return 2
    if n == 2:
        return 4
    return another_complex_sequence(n - 1) * another_complex_sequence(n - 2) % 100


assert another_complex_sequence(5) == 56
