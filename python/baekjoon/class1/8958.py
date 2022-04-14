if __name__ == "__main__":

    for i in range(int(input())):
        total = []
        count = 0
        results = list(input())

        for result in results:
            if result == "O":
                total.append(count + 1)
                count += 1
            else:
                count = 0
                total.append(0)

        print(sum(total))
