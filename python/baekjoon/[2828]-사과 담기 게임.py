n, m = map(int, input().split())

k = int(input())

moves = 0

left = 1

for _ in range(k):
    where = int(input())
    right = left + m - 1
    # 1. 떨어지는 사과가 바구니 영역에 들어올때
    if where >= left and where <= right:
        continue
    # 2. 사과가 바구니 왼편에 떨어질때
    if where < left:
        moves += (left - where)
        left = where
    # 3. 사과가 바구니 오른편에 떨어질때
    else:
        moves += (where - right)
        left += (where - right)

print(moves)
