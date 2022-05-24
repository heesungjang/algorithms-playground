"""
여러 알고리즘 문제를 풀다 보면 시간과 날짜를 계산해야 하는 경우가 종종 있다.

흐르는 시간과 날짜를 계산하는 예제들을 살펴보자.

2시 5분에서 4시 1분이 되려면 몇 분이 흘러야 하는지를 어떻게 계산해 볼 수 있을까?
"""

# 예시) 시물레이션
hour, mins = 2, 5

elapsed_mins = 0

while True:
    if hour == 4 and mins == 1:
        break

    elapsed_mins += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(elapsed_mins)

"""
이런 경우  0시 0분에서 시작하여 각 시간까지 걸리는 분을 계산하고,

그 차이를 계산하는 식으로 진행하면 시뮬레이션을 직접 진행하지 않더라도 답을 쉽게 구할 수 있다.

1. 예시) 2011년 11월 11일 a시 b분에서 시작하여 2011년 11월 11일 c시 d분까지 몇 분이 걸리는지를 계산 해보자.
"""

input = [2, 5, 4, 1]

h1, m1, h2, m2 = input

# from 0시 00분 to h2시 m2분
elpased_mins = (h2 * 60 + m2) - (h1 * 60 + m1)

print(elpased_mins)

"""
특점 시점에서 얼마만큼 흐른 날짜를 계산하는 방법도 같은 개념으로 쉽게 계산이 가능하다.
"""


# 예시) 시물레이션

def get_elapsed_date_from_2월_5일(m, d):
    month, day = 2, 5
    elapsed_days = 0
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:
        if month == m and day == d:
            break

        elapsed_days += 1
        day += 1

        if day > num_of_days[month]:
            month += 1
            day = 1

    return elapsed_days


assert get_elapsed_date_from_2월_5일(4, 1) == 55

"""
2011년 m1월 d1일로부터 2011년 m2월 d2일까지, 
총 몇 일이 있는지를 계산하는 프로그램을 작성해자.

2011년은 윤년이 아닌 해이기 때문에 2월은 28일까지 있다.

tip) 
1. 흐르는 날짜를 계산할 때에는, 직접 시물레이션을 하기 보다는 1월 1일에서 시작하여 각 날짜까지 총 몇일이 있는지를
2. 구한 뒤 그 차이를 계산하는 식으로 답을 찾는것이 편리하다.
"""


def num_of_days(m, d):
    total_days = 0
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(1, m):
        total_days += days[i]

    total_days += d

    return total_days


def get_elapsed_date_from(m1, d1, m2, d2):
    elapsed_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
    return elapsed_days


assert get_elapsed_date_from(3, 5, 5, 2) == 59

"""
위 개념을 응용해서 조금 더 복잡한 시간 관련 문제를 풀어보자.

문제)
2011년 m1월 d1일이 월요일 이었다면, 2011년 m2월 d2은 어떤 요일인지를 구하는 프로그램을 작성해보자. 

2011년은 윤년이 아닌 해이기 때문에 2월은 28일까지 있다.
"""


def get_which_day(m1, d1, m2, d2):
    day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    diff = num_of_days(m2, d2) - num_of_days(m1, d1)
    print(diff)
    """
    여기서 예로 2월 2일에서 2월 1일로 간다고 하면 result_days는 -1이 될 것이다.
    2월 2일은 월요일이므로, 답은 일요일이 되어야 하고
    -1의 의미는 곧 뒤로 하루 가야 한다는 뜻이므로, 요일이 변하지 않기 위해서는 양수가 될 때까지 계속 7의 배수를 더해줘야 한다.
    """
    while diff < 0:
        diff += 7

    return day_of_week[diff % 7]


assert get_which_day(5, 4, 5, 3) == "Sun"
