n = 15

counter = 0  # 나눗셈 횟수 카운트
ptr = 0  # 이미 찾은 소소의 개수
prime = [None] * n  # 소수를 정장하는 배열
prime[ptr] = 2
ptr += 1

for i in range(3, n + 1, 2):  # 4이상의 짝수는 소수가 아님 / 4 또한 소수가 아님
    for j in range(1, ptr):  # 이미 찾은 소수의 개수 길이 만큼
        counter += 1
        if i % prime[j] == 0:
            break
    else:
        prime[ptr] = i
        ptr += 1

for i in range(ptr):
    print(prime[i])
