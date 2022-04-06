if __name__ == "__main__":
    a, b = [int(num) for num in input().split()]

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")
