while True:
    a, b = [int(num) for num in input().split()]

    if a + b == 0:
        break
    else:
        print(a + b)
