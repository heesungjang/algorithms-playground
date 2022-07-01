n = int(input())

target = 666
cnt = 0
while n:
    if "666" in str(target):
        cnt += 1
        if cnt == n: break
    target += 1
print(target)
