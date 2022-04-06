if __name__ == "__main__":
    # 구구단 N단
    n = int(input())

    for i in range(1, 10):
        calculated_value = n * i

        print(f"{n} * {i} = {calculated_value}")
