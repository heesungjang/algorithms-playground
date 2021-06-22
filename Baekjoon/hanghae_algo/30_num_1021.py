from collections import deque

N, M = map(int, input().split())
li = list(map(int, input().split()))
queue = deque(range(1, N+1))
cnt = 0
for n in li:
    while queue[0] != n:
        t = queue.index(n)
        if t <= len(queue)-t-1:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
        cnt += 1
    queue.popleft()
print(cnt)