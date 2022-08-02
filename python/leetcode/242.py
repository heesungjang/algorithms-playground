s = "a"
t = "ab"


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    Sdic = {}
    Tdic = {}

    for char in s:
        if char in Sdic:
            Sdic[char] += 1
        else:
            Sdic[char] = 1

    for char in t:
        if char in Tdic:
            Tdic[char] += 1
        else:
            Tdic[char] = 1

    for key in Sdic.keys():
        if key not in Tdic:
            return False

        if Sdic[key] != Tdic[key]:
            return False

    return True


print(isAnagram(s, t))
