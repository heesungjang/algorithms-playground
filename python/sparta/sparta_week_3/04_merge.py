"""
4. merge 정별 방법
"""
array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    for i in range(len(array_a)):
        new_array = []
        array1_index = 0
        array2_index = 0
        while array1_index < len(array_a) and array1_index < len(array_b):
            if not array_a[array1_index] >= array_b[array2_index]:
                new_array.append(array_a[array1_index])
                array1_index += 1
            else:
                new_array.append(array_b[array2_index])
                array2_index += 1
        if array1_index == len(array_a):
            while array2_index < len(array_b):
                new_array.append(array_b[array2_index])
                array2_index += 1

        if array2_index == len(array_b):
            while array1_index < len(array_a):
                new_array.append(array_a[array1_index])
                array1_index += 1
        return new_array
    return


print(merge(array_a, array_b))  # 출력 = [1, 2, 3, 4, 5, 6, 7, 8]
