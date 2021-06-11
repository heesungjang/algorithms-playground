def find_alphabet_occurrence_array(string):
    """
    1. is.alpha()  return true or false if alphabet

    2. ord() return ASCII number for string

    3. we have list of 0s in list
    """
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if  not char.isalpha():
            continue
        alpha_index = ord(char) - ord("a")
        alphabet_occurrence_array[alpha_index] += 1
    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))
