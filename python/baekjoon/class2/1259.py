if __name__ == "__main__":
    def is_palindrome(num: int) -> None:
        nums = [int(n) for n in str(num)]

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                print("no")
                return

        print("yes")


    while True:
        num = int(input())
        if num > 0:
            is_palindrome(num)
        else:
            break
