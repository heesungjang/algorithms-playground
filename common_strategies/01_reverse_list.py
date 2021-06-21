from typing import Any, MutableSequence

arr_numbers = [1, 2, 3, 4, 5, 6, 7]


def reverse_array(arr: MutableSequence) -> Any:
    n = len(arr_numbers)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


print(arr_numbers)
reverse_array(arr_numbers)
print(arr_numbers)
