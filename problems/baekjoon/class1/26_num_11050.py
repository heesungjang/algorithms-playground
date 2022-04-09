import sys

N, K = map(int, sys.stdin.readline().split(" "))
K = min(K, N-K)
up, down = 1, 1

for i in range(1, K+1):
    up *= (N-i+1)
    down *= i

print(up//down)