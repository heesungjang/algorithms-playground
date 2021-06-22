word = input().upper()
dic = {}

for i in word:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
max_cnt = max(dic.values())
result = []
for key, value in dic.items():
    if value == max_cnt:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print('?')