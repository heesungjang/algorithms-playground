"""
3. 삽입 정렬
"""
input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(input)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return


insertion_sort(input)
print(input)  # 출력 = [1, 2, 4, 6, 9]
