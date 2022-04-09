if __name__ == "__main__":
    n = int(input())
    scores = [int(num) for num in input().split()]

    highest = max(scores)

    sum = 0
    for score in scores:
        sum += score / highest * 100

    print(sum / n)
