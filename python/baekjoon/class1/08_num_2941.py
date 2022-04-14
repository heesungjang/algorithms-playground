word_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
W = input()

for i in word_list:
    W = W.replace(i, '*')

print(len(W))