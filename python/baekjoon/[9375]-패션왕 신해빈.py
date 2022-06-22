n = int(input())

for _ in range(n):
    c_nums = int(input())  # 의상의 수

    if c_nums == 0:
        print(0)
        continue

    c_dic = {}  # 의상의 타입이 몇개인지 카운트

    for _ in range(c_nums):
        c_name, c_type = list(input().split())

        if c_type not in c_dic:
            c_dic[c_type] = 1
        else:
            c_dic[c_type] += 1

    answer = 1

    for v in c_dic.values():
        answer *= v + 1

    print(answer - 1)
