input = "hello my name is sparta"

alphabet_occurrence_array = [0] * 26


def find_max_occurred_alphabet(string):
    for char in string:
        if not char.isalpha():
            continue
        alpha_index = ord(char) - ord("a")
        alphabet_occurrence_array[alpha_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence += alphabet_occurrence

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)

print(result)
