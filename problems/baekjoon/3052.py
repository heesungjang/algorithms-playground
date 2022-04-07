if __name__ == "__main__":
    remainders = set()

    for i in range(10):
        remainders.add(int(input()) % 42)

    print(len(list(remainders)))
    