def get_gcd(num1: int, num2: int) -> int:
    gcd = 0  # 최대 공약수 초기화

    # 공약수가 작은 수의 약수보다 클 수 없기 때문에 min(num1, num2)
    # 반복문을 실행하면서 -> 가장 마지막 공약수가 = gcd(최대 공약수)
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd


assert get_gcd(12, 18) == 6
assert get_gcd(24, 36) == 12
