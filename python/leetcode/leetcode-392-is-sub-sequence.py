from typing import List

string = "abc"
target = "ahbgdc"


def is_suq_sequence(s: str, t: str):
    s_pointer = 0
    t_pointer = 0

    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
            t_pointer += 1
        else:
            t_pointer += 1

    if s_pointer < len(s):
        return False

    return True


print(is_suq_sequence(string, target))
