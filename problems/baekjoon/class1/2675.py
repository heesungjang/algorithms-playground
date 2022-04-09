if __name__ == "__main__":
    # test case number
    n = int(input())

    for i in range(n):
        # a = 반복 횟수: str
        # b = 문자열: str
        num, string = input().split()

        text = ""
        for char in string:
            text += int(num) * char

        print(text)
