from typing import List

lst = [5, 1, 2, 3, 7, 9, 11]


def selection_sort(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]

    return data


result_1 = selection_sort(lst)

print(result_1)

lst = [5, 1, 2, 3, 7, 9, 11]


def exchange_sort(data) -> List[int]:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]

    return data


result_2 = exchange_sort(lst)
print(result_2)
