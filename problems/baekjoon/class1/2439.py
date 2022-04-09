if __name__ == "__main__":
    n = int(input())

    init = [" " for _ in range(n)]

    for i in range(n):
        init[i] = '*'
        reversed_list = list(reversed(init))

        print("".join(reversed_list))
