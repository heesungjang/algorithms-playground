if __name__ == "__main__":
    nums = [int(num) for num in input().split()]

    total_sum = 0

    for num in nums:
        total_sum += (num * num)

    print(total_sum % 10)
