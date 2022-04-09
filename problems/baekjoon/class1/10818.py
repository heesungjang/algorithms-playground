if __name__ == "__main__":
    n = int(input())
    nums = [int(num) for num in input().split()]

    nums.sort()

    print(nums[0], nums[-1])
