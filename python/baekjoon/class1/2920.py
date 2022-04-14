if __name__ == "__main__":
    nums = [int(num) for num in input().split()]

    if nums == sorted(nums):
        print("ascending")
    elif nums == sorted(nums, reverse=True):
        print("descending")
    else:
        print("mixed")
