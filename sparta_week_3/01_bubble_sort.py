"""
1. 버블 정렬
  -> -> -> ->
[4, 6 ,2, 9 ,1]
  -> -> ->
[4, 2 ,6, 1, 9]
  -> ->
[2, 4 ,1, 6, 9]
  ->
[2, 1 ,4, 6, 9]
"""

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(input)
print(input)  # 출력 = [1, 2, 4, 6, 9]
