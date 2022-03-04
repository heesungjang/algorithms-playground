"""
2. 선택 정렬

[4, 6, 2, 9, 1]
 -  -  -  -  -
[1, 6, 2, 9, 4]
    -  -  -  -
[1, 2, 6, 9, 4]
       -  -  -
[1, 2, 4, 9, 6]
          -  -
[1, 2, 4, 6, 9]
"""
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(input)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if input[i + j] < input[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]


# i = 0 1 2 3          # i = 0 1 2 3
# j = 0 1 2 3          # j = 0 1 2 3 4  i+j = 01234
# j = 0 1 2            # j = 0 1 2 3  i+j = 1234
# j = 0 1              # j = 0 1 2  i+j = 234
# j = 0                # j = 0 1  i+j = 34

selection_sort(input)
print(input)  # 출력 = [1, 2, 4, 6, 9]
