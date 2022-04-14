while True:
    try:
        a, b = [int(num) for num in input().split()]
        print(a + b)
    except:
        break
