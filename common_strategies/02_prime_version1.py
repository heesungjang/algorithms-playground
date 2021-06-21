
from typing import MutableSequence, Any

n = 15
count = 0
for i in range(2, n+1):
    for j in range(2, i):
        count += 1
        if i % j == 0:
            break
    else:
        print(i)

print(count)

