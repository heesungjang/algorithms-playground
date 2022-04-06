if __name__ == "__main__":
    a, b, c = [int(input()) for _ in range(3)]

    multiplied_value = str(a * b * c)

    # 0 부터 9까지 반복문 실행
    for i in range(10):
        count = list(map(int, list(multiplied_value))).count(i)
        print(count)
