if __name__ == "__main__":
    a, b = input().split()

    print(max(int(a[::-1]), int(b[::-1])))
