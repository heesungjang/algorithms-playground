def divide(a: int, b: int):
    return a / b


if __name__ == "__main__":
    a, b = [int(num) for num in input().split()]
    result = divide(a, b)
    print(result)
