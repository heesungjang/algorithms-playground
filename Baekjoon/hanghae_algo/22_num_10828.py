import sys

n, s, r = input(), [], []
com = sys.stdin.readlines()
for x in com:
    c = x.split()
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == 'pop':
        if len(s) == 0:
            r.append('-1')
        else:
            r.append(s.pop(-1))
    elif c[0] == 'size':
        r.append(str(len(s)))
    elif c[0] == 'empty':
        if len(s) == 0:
            r.append('1')
        else:
            r.append('0')
    elif c[0] == 'top':
        if len(s) == 0:
            r.append('-1')
        else:
            r.append(s[-1])
print("\n".join(r))
