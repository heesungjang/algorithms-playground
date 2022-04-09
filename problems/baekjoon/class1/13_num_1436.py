n = int(input())
count_for_n = 0
target_number = 666
while True:
    if '666' in str(target_number):
        count_for_n += 1
    if count_for_n == n:
        print(target_number)
        break
    target_number += 1


