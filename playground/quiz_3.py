# ----------------------------------------------
# Quiz 3 (Lessons 4 - 6)
#
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs.
# The test function will print 'OK' when your function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# ----------------------------------------------
# Part A:  Conditionals
#   Each function below has a docstring which explains its interface.
#   Add code to implement the expected functionality
#
#   The solution for Question a1() has been provided for you as an example.
# ----------------------------------------------
import collections


def a1(x):
    """ Given an integer number x, returns:
        0, if x is negative or 0
        x, if x is strictly positive and less than or equal to 10
        10, otherwise """
    if x <= 0:
        return 0
    elif x <= 10:
        return x

    return 10


def a2(x, y):
    """ Given two integer numbers x and y, returns:

        2x + y, if x is strictly greater than y
        4y - 3, if y is strictly greater than x
        x^3 + xy, if x is equal to y """
    if x > y:
        return 2 * x + y
    elif x < y:
        return 4 * y - 3
    else:
        return x ** 3 + (x * y)


def a3(x, y, z):
    """ Given three integer numbers x, y, and z, returns:

        0, if any of the two numbers are the same
        1, if the numbers are ordered such that x < y and y < z
        2, otherwise """
    if x < y < z:
        return 1
    else:
        if x == y or x == z or y == z:
            return 0

    return 2


def a4(x, y, z, w):
    """ Given four integer numbers x, y, z, and w, returns:

        the maximum of a2(x, y) and a2(z, w), if x is strictly less than y
        the sum of a3(z, y, x) and a1(w), otherwise """

    if x < y:
        return max(a2(x, y), a2(z, w))
    else:
        return a3(z, y, x) + a1(w)


# ----------------------------------------------
# Part B:  Iteration
#   Each function below has a docstring which explains its interface.
#   Add code to implement the expected functionality
# ----------------------------------------------
def b1(x):
    """ Given an integer number n, returns:
        True: if each digit of n is an even number,
        False: if any digit is odd """

    strs = str(x)
    for int_num in strs:
        if int(int_num) % 2 == 0:
            return True
        else:
            return False


def b2():
    """ Return a string which will print the alphabet pattern 'A', shown below.
        Use loops and conditional statements, do NOT just hard code the text string.
		The letter fits in a 7x7 grid

          ***
         *   *
         *   *
         *****
         *   *
         *   *
         *   *
    """
    result = ""
    for i in range(7):
        if i == 0:
            result += f"  {'*' * 3}  \n"
        elif i == 3:
            result += " ***** \n"
        else:
            result += " *   * \n"

    return result


def b3():
    """ Return a string which will print the alphabet pattern 'G', shown below.
        Use loops and conditional statements, do NOT just hard code the text string.
		The letter fits in a 7x7 grid

          ***
         *   *
         *
         * ***
         *   *
         *   *
          ***
    """
    result = ""
    for i in range(7):
        if i == 0 or i == 6:
            result += "  ***  \n"
        elif i == 2:
            result += " *     \n"
        elif i == 3:
            result += " * *** \n"
        else:
            result += " *   * \n"

    return result


def b4(start, end, k):
    """ Returns the sum of every k-th number between start and end.
        You can assume start <= end and that k > 0.
        For example:

        b4(1, 10, 3) returns 1 + 4 + 7 + 10 = 22

        You are NOT permitted to use the math library
        """
    sum = 0
    for i in range(start, end + 1, k):
        sum += i

    return sum


# ----------------------------------------------
# Part C:  Incremental development and Recursion
#   Each function below has a docstring which explains its interface.
#   Add code to implement the expected functionality
# ----------------------------------------------
def c1_loop(n):
    """ Given an non-negative integer number n, return:
        the sum of its digits.
        Use loops within the function for this version. """

    num_list = [int(char) for char in str(n)]

    sum = 0

    for num in num_list:
        sum += num

    return sum


def c1_rec(n):
    """ Given an non-negative integer number n:
        write a recursive function that returns the sum of its digits.
    """

    num_list = [int(char) for char in str(n)]

    def get_sum(num_list):
        if len(num_list) == 0:
            return 0
        return (num_list[0]) + get_sum(num_list[1:])

    return get_sum(num_list)


def c2_loop(n):
    """ Given an non-negative integer number n, return:
        calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x <= 0).
        Use loops within the function for this version. """
    sum = n
    i = 2
    while n - i >= 0:
        sum += (n - i)
        i += 2

    return sum


def c2_rec(n):
    """ Given an non-negative integer number n:
        write a recursive function that calculates the sum of the positive i
        ntegers of n+(n-2)+(n-4)... (until n-x =< 0)
    """

    def get_sum(n):
        if n < 1:
            return 0

        return n + get_sum(n - 2)

    return get_sum(n)


# ----------------------------------------------
# Test functions
# ----------------------------------------------

def test(name, got, expected):
    """ Simple test() function, called in main().  Prints status of test.
    If got doesn't match expected, error messages is displayed.
    """
    if got == expected:
        print(name + ' - OK')
    else:
        print('%s - X got: %s expected: %s' % (name, repr(got), repr(expected)))


def main():
    """ Test exercise functions above using test function
    """
    print()
    print('Part A: Conditionals\n')
    test('a1(-3)', a1(-3), 0)
    test('a1(5)', a1(5), 5)
    test('a1(42)', a1(42), 10)
    test('a2(5, 4)', a2(5, 4), 14)
    test('a2(9, 10)', a2(9, 10), 37)
    test('a2(2, 2)', a2(2, 2), 12)
    test('a3(5, 4, 4)', a3(5, 4, 4), 0)
    test('a3(4, 4, 4)', a3(4, 4, 4), 0)
    test('a3(4, 4, 5)', a3(4, 4, 5), 0)
    test('a3(4, 5, 4)', a3(4, 5, 4), 0)
    test('a3(1, 2, 3)', a3(1, 2, 3), 1)
    test('a3(-1, 2, 3)', a3(-1, 2, 3), 1)
    test('a3(4, 3, 2)', a3(4, 3, 2), 2)
    test('a3(1, 2, 0)', a3(1, 2, 0), 2)
    test('a4(1, 2, 0, 10)', a4(1, 2, 0, 10), 37)
    test('a4(0, 0, 0, 12)', a4(0, 0, 0, 12), 10)
    test('a4(1, 1, 0, 12)', a4(1, 1, 0, 12), 10)

    print()
    print('Part B: Iteration and Logical operators\n')
    test('b1(222)', b1(222), True)
    test('b1(3024)', b1(3024), False)
    a = '  ***  \n'
    a += ' *   * \n'
    a += ' *   * \n'
    a += ' ***** \n'
    a += ' *   * \n'
    a += ' *   * \n'
    a += ' *   * \n'
    test('b2()', b2(), a)

    g = '  ***  \n'
    g += ' *   * \n'
    g += ' *     \n'
    g += ' * *** \n'
    g += ' *   * \n'
    g += ' *   * \n'
    g += '  ***  \n'
    test('b3()', b3(), g)

    test('b4(1, 10, 3)', b4(1, 10, 3), 22)
    test('b4(1, 5, 6)', b4(1, 5, 6), 1)
    test('b4(4, 9, 2)', b4(4, 9, 2), 18)
    test('b4(-4, 8, 5)', b4(-4, 8, 5), 3)

    print()
    print('Part C: Incremental development/Recursion\n')
    test('c1_loop(345)', c1_loop(345), 12)
    test('c1_loop(45)', c1_loop(45), 9)
    test('c1_rec(345)', c1_rec(345), 12)
    test('c1_rec(45)', c1_rec(45), 9)
    test('c2_loop(1)', c2_loop(1), 1)
    test('c2_loop(6)', c2_loop(6), 12)
    test('c2_loop(10)', c2_loop(10), 30)
    test('c2_rec(1)', c2_rec(1), 1)
    test('c2_rec(6)', c2_rec(6), 12)
    test('c2_rec(10)', c2_rec(10), 30)


# Call the main() function
if __name__ == '__main__':
    main()
