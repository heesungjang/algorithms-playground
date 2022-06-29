vowel = ["a", "e", "i", "o", "u"]


def continuous_3(word):
    for i in range(len(word) - 2):
        if word[i] in vowel and word[i + 1] in vowel and word[i + 2] in vowel:
            return True
        elif word[i] not in vowel and word[i + 1] not in vowel and word[i + 2] not in vowel:
            return True


def continuous_2(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1] and word[i:i + 2] != "ee" and word[i:i + 2] != "oo":
            return True


def go():
    while True:
        psw = input()
        if psw == "end":
            break

        # 1. 모음 하나 반드시 포함
        if not any(char in list(psw) for char in vowel):
            print(f"<{psw}> is not acceptable.")
            continue

        # 연속된 3 자음, 3 모음 x
        if continuous_3(psw):
            print(f"<{psw}> is not acceptable.")
            continue

        if continuous_2(psw):
            print(f"<{psw}> is not acceptable.")
            continue

        print(f"<{psw}> is acceptable.")


go()
