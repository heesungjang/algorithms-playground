def solution(numbers, hand):
    answer = ''
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    crr_lh = "*"
    curr_rh = "#"

    for i in numbers:
        if i in left:
            answer += "L"
            curr_lh = i
        elif i in right:
            answer += "R"
            curr_rh = i
        else:
            curPos = keypad[i]
            lPos = keypad[curr_lh]
            rPos = keypad[curr_rh]
            ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if ldist < rdist:
                answer += "L"
                curr_lh = i
            elif ldist > rdist:
                answer += "R"
                curr_rh = i
            else:
                if hand == "left":
                    answer += "L"
                    curr_lh = i
                else:
                    answer += "R"
                    curr_rh = i

    return answer
