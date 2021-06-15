def count_down(number):
    if number < 0:
        return
    count_down(number - 1)
    print(number)


count_down(60)
