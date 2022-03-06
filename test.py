a = []

for i in range(1, 10 + 1):
    if i % 2 == 1:
        a.append(i * 2)

print(a)

b = [i * 2 for i in range(1, 10 + 1) if i % 2 == 1]

print(b)

original = {"heesung": 12, "zion": "13"}

c = {}

for key, value in original.items():
    c[key] = value

print(c)

first_list = list(range(1, 5 + 1))

print(first_list)

second_list = enumerate(first_list)

print(list(second_list))

third_list = [1, 2, 3, 4, 5]

for (i, v) in enumerate(third_list):
    print(i, v)

print(divmod(5, 2))

test = [1]

if test:
    print("yes")
else:
    print("no")
