def add(a: int, b: int):
    return a + b


if __name__ == "__main__":
    a, b = [int(num) for num in input().split()]
    result = add(a, b)
    print(result)
