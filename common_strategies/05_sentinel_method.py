import copy

lst = [1, 2, 3, 4, 5]


def seq_search(seq, key):
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0

    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i


result = seq_search(lst, 3)

if result == -1:
    print("Searching failed")
else:
    print(f"position: {result}")
print(result)
