def function1(listN):
    """
    function 1 takes list of digits as an argument

    based on the last digit number of a student number,
    it generates return value accordingly to specification table
    """
    my_student_id = "u1151023"
    last_digit_number = int(my_student_id[-1])

    # case 1
    if last_digit_number == 1:
        sorted_list_num = sorted(listN)
        second_largest_num = sorted_list_num[-2]

        return second_largest_num
    # case 2
    elif last_digit_number == 2:
        max_value = max(listN)
        max_value_idx = listN.index(max_value)

        return max_value_idx
    # case 3
    elif last_digit_number == 3:
        avg_list_num = sum(listN) / len(listN)

        return avg_list_num
    # case 4
    elif last_digit_number == 4:
        min_value = min(listN)
        min_value_idx = listN.index(min_value)

        return min_value_idx
    # case 5
    elif last_digit_number == 5:
        sorted_list_num = sorted(listN)
        third_smallest = sorted_list_num[2]

        return third_smallest
    # case 6
    elif last_digit_number == 6:
        sum_of_last_three = sum(listN[-3:])

        return sum_of_last_three
    # case 7
    elif last_digit_number == 7:
        avg_of_second_forth = (listN[1] + listN[3]) / 2

        return avg_of_second_forth
    # case 8
    elif last_digit_number == 8:
        mod_of_sixth_second = listN[5] % listN[1]

        return mod_of_sixth_second
    # case 9
    elif last_digit_number == 9:
        mod_of_third_last = listN[2] % listN[-1]

        return mod_of_third_last
    # case 0
    else:
        remainder = listN[4] / listN[0]

        return remainder


def function2(result):
    """
    Function 2 prompt user to guess the return value of function 1.

    user are only given 3 chances for guessing

    if all chances are used, function terminates and return False,
    indicating user have failed to guess the return value
    """
    my_student_id = "u1151023"
    last_digit_number = int(my_student_id[-1])

    result = str(result)
    # specification for last digit numbers from 1~3
    if last_digit_number in [1, 2, 3]:
        for i in range(1, 3 + 1):
            user_guess = input("Please guess correct return value of function1: ")

            if user_guess == result:
                print(
                    f"The return value of function1 is {result} , "
                    f"the user got the correct answer in the {i} attempt")
                return
            else:
                continue
        print(f"The return value of function1 is {result}, "
              "the user did not get the correct answer in three times")

    # specification for last digit numbers from 4~7
    elif last_digit_number in [4, 5, 6, 7]:
        for i in range(1, 3 + 1):
            user_guess = input("Please guess correct return value of function1: ")
            if user_guess == result:
                print(f"""
                - Return value of function 1 is {result}
                - User has {3 - i} choices to guess the correct value
                - User got the correct answer
                """)
                return
            else:
                continue
        print(f"""
        - Return value of function 1 is {result}
        - User has 0 choices to guess the correct value
        - User did not get the correct answer
        """)

    # specification for last digit numbers from 8~0
    elif last_digit_number in [8, 9, 0]:
        for i in range(1, 3 + 1):
            user_guess = input("Please guess correct return value of function1: ")
            if user_guess == result:
                print(f"""
                1. Return value of function 1 is {result}
                2. Did user get the correct answer in three times? Yes
                """)
                return
            else:
                continue
        print(f"""
        1. Return value of function 1 is {result}
        2. Did user get the correct answer in three times? No
        """)


listNumber = [3, 2, 5, 7, 9, 8, 6, 0, 1, 4]
resultFromF1 = function1(listNumber)
function2(resultFromF1)


def isGoodID(l_num):
    """
    this function takes licence number(str) as an argument.

    It then validates the licence number and returns boolean value
    True if validate number
    False if not validate number
    """

    # 1. consisting of 3 digits.
    # 2. Each of the 3 digit sequences is separated by a "-".
    sub_strings = l_num.split("-")

    if len(sub_strings) != 3:
        return False
    for sub_string in sub_strings:
        if len(sub_string) != 3:
            return False

    # 3. The first digit for the first 3 digit sequence not "0"
    if sub_strings[0][0] == "0":
        return False

    # 4. The last digit for the second 3 digit sequence is an odd number.
    if int(sub_strings[1][-1]) % 2 == 0:
        return False

    # 5. At least two digits of the driver's licence number are the same
    numbers = [num for num in l_num if num.isnumeric()]
    repeated = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                repeated += 1
    if repeated == 0:
        return False

    # 6. No digit appears more than three times (e.g. "113-099-994" is invalid).
    for i in range(len(numbers)):
        cnt = 0
        for j in range(len(numbers)):
            if numbers[j] == numbers[i]:
                cnt += 1
        if cnt > 3:
            return False
    return True


licence_number = "113-099-263"
isGoodID(licence_number)


def isGoodDate(date):
    """
    this function takes user input for birthdate(str) and validate
    if the date is in format of yyyy-mm-dd

    returns boolean value
    """
    if len(list(date.split("-"))) < 3:
        return False

    y, m, d = list(date.split("-"))
    if len(y) != 4:
        return False
    if len(m) != 2:
        return False
    if len(d) != 2:
        return False

    if int(m) > 12 or int(m) < 1:
        return False
    if int(d) > 31 or int(d) < 1:
        return False
    return True


records = []
while True:
    while True:
        permit_number = input("Please enter your permit number (9 digit number) or 'END'' to finish: ")
        if permit_number == "END":
            break
        if not permit_number.isnumeric() or len(permit_number) < 9:
            print("Please enter valid permit number")
            continue
        else:
            break
    if permit_number == "END":
        break

    while True:
        firstName = input("Enter the given name of a driving student of the school: ")
        if not firstName:
            print("You can't leave first name empty, try again.")
            continue
        else:
            break
    firstName.strip()
    firstName = firstName.strip(" ")

    while True:
        lastName = input("Enter the given name of a driving student of the school: ")
        if not lastName:
            print("You can't leave first name empty, try again.")
            continue
        else:
            break
    lastName.strip()
    lastName = lastName.strip(" ")

    while True:
        date_of_birth = input("Please enter date of birth in following format, yyyy-mm-dd: ")
        if not isGoodDate(date_of_birth):
            print("Please enter validate date")
            continue
        else:
            break

    new_record = [lastName, firstName, date_of_birth, permit_number]

    records.append(new_record)

# sort first by last name[0] and first name[1]
records.sort(key=lambda x: (x[0], x[1]))

for r in records:
    print(f"""
    given name: {r[1]}
    surname: {r[0]}
    birth date: {r[2]}
    permit no: {r[-1]}
    """)
