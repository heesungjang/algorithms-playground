strs = list(input())

for i, s in enumerate(strs):
    if s.islower():
        strs[i] = chr((97 + (ord(s) + 13 - 97) % 26))
    elif s.isupper():
        strs[i] = chr((65 + (ord(s) + 13 - 65) % 26))

print("".join(strs))
