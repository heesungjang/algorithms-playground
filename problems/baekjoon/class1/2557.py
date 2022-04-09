if __name__ == "__main__":
    nums = []

    for i in range(9):
        nums.append(int(input()))

    max_value = max(nums)
    max_index = nums.index(max_value)

    print(max_value)
    print(max_index + 1)
