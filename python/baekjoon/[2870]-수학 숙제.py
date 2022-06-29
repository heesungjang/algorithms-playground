# n = int(input())  # 종이의 줄의 개수
#
# answer = []
#
# for _ in range(n):
#     word = list(input())
#
#     while word:
#
#         # 마지막에 남은 수가 0이면 담고
#         if len(word) == 1 and word[0] == "0":
#             word.pop()
#             answer.append("0")
#             continue
#
#         # 시작이 0이거나 알파벳이면 제거
#         if word[0].isalpha() or (word[0] == "0" and word[1] != "0"):
#             word = word[1:]
#             continue
#
#         cnt = 0
#
#         num = ""
#         for i in range(len(word)):
#             if word[i].isalpha():
#                 break
#             if word[i].isnumeric():
#                 cnt += 1
#                 num += word[i]
#         answer.append(num)
#
#         word = word[cnt + 1:]
#
# answer = sorted(list(map(int, answer)))
#
# for n in answer:
#     print(n)

ans = []
for _ in range(int(input())):
    S = input()
    tmp = ''
    for i in S:
        if 97 <= ord(i) <= 122:
            if tmp:
                ans.append(int(tmp))
                tmp = ''
            else:
                tmp = ''
        else:
            tmp += i
    if tmp:
        ans.append(int(tmp))
ans.sort()
for i in ans:
    print(i)