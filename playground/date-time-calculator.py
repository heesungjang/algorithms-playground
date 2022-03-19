"""
validating user input and encapsulating functions
https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
"""
import datetime, time

SECONDS_IN_YEAR = 365 * 60 * 60 * 24
SECONDS_IN_DAY = 60 * 60 * 24
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60


def determine_leap(year: int) -> bool:
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    # not divided by 100 means that it's not a century years
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False


def get_event_name(prompt: str) -> str:
    """
    Prompt user to enter the event name

    Repeat the prompt if:
    1. type of event name is not a string
    2. empty event name
    :return: event name (str)
    """

    input_name = ""
    while True:
        input_name = input(prompt)
        if not input_name:
            print("You can not leave event name empty, please try again. \n")
            continue
        else:
            break
    return input_name


def get_event_year(prompt: str) -> int:
    """
    prompt user to enter the year of the event

    Repeat the prompt if:
    1. type of event year is not a number
    2. if entered event year is before 1970
    :return: event year (int)
    """

    input_year = 0
    while True:
        try:
            input_year = int(input(prompt))
        except ValueError:
            print("Please enter a valid number for event year \n")
            continue

        if input_year <= 1970:
            print("Year of the event needs to be past 1970, e.g) 1971 \n")
            continue
        else:
            break

    return input_year


def get_event_month(prompt: str) -> int:
    """
    prompt user for the month of the event

    Repeat the prompt if:
    1. type of event month is not a number
    2. if entered month is out of range (1-12)

    :return: event month (int)
    """

    input_month = 0
    while True:
        try:
            input_month = int(input(prompt))
        except ValueError:
            print("Please enter a valid number for event month \n")
            continue

        if input_month < 1 or input_month > 12:
            print("Please enter month between 1-12 \n")
            continue
        else:
            break
    return input_month


def get_event_day(prompt: str, year, month) -> int:
    """
    prompt user for the event day

    Repeat the prompt if:
    1. the type of entered event day is not a number
    2. entered day is out of range for particular month

    :return: event day (int)
    """
    input_day = 0
    leap_year = determine_leap(year)

    while True:
        try:
            input_day = int(input(prompt))
        except ValueError:
            print("Please enter a valid number for event day \n")
            continue

        if input_day < 1 or input_day > 31:
            print("Please enter the day value between 1-31 \n")
            continue

        if not leap_year and month == 2 and input_day > 28:
            print(f"There are only 28 days in {year}, February. Please try again! \n")
            continue
        elif leap_year and month == 2 and input_day > 29:
            print(f"There are only 29 days in {year}, February. Please try again! \n")
            continue

        if month in [4, 6, 9, 11] and input_day > 30:
            print("There are only 30 days in current month, please try again! \n")
            continue
        else:
            break

    return input_day


event_name = get_event_name("Enter the name of event: ")
event_year = get_event_year("Enter the year of the event: ")
event_month = get_event_month("Enter the month of the event, e.g. 1-12: ")
event_day = get_event_day("Enter the day of your event, e.g. 1-31: ", event_year, event_month)

event_time = datetime.datetime(event_year, event_month, event_day)
event_time_in_seconds = time.mktime(event_time.timetuple())

current_time_in_seconds = time.time()

# time difference between current time and event time
time_difference = abs(event_time_in_seconds - current_time_in_seconds)

# event is from past if time difference is negative, vice versa if positive.
is_future = event_time_in_seconds - current_time_in_seconds > 0

years_to_event = int(time_difference // SECONDS_IN_YEAR)

days_to_event = int((time_difference % SECONDS_IN_YEAR) // SECONDS_IN_DAY)

hours_to_event = int((time_difference % SECONDS_IN_DAY) // SECONDS_IN_HOUR)

minutes_to_event = int((time_difference % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)

seconds_to_event = int(time_difference % SECONDS_IN_MINUTE)

# mapped months words in english for print statement.
month_map = {1: "January", 2: "February", 3: "March",
             4: "April", 5: "May", 6: "June",
             7: "July", 8: "August", 9: "September",
             10: "October", 11: "November", 12: "December"}

print(
    f'{event_name} {"is" if is_future else "was"} on {event_day} {month_map[event_month]} {event_year} '
    f'({years_to_event} years, {days_to_event} days, {hours_to_event} hours, '
    f'{minutes_to_event} minutes and {seconds_to_event} seconds {"later" if is_future else "ago"}).')
