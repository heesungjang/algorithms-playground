N = int(input())

group = 0
for i in range(N):
    Num = input()
    cnt = 0
    for j in range(len(Num) - 1):
        if Num[j] != Num[j + 1]:
            Num_list = Num[j + 1:]
            if Num_list.count(Num[j]) > 0:
                cnt += 1
    if cnt == 0:
        group += 1
print(group)

