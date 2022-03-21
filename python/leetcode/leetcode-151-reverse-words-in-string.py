from pprint import pprint

input1 = "  hello world  "
input2 = "the sky is blue"
input3 = "a good   example"


def reverse_words(s: str) -> str:
    # stack = []
    # temp_string = ""
    #
    # for char in s.strip():
    #     if len(temp_string) == 0 and char == " ":
    #         continue
    #
    #     if char != " ":
    #         temp_string += char
    #         continue
    #     else:
    #         stack.append(temp_string)
    #         temp_string = ""
    #         continue
    # stack.append(temp_string)
    # stack.reverse()
    # print(stack)
    # print(" ".join(stack))
    words = s.strip().split(" ")
    words.reverse()
    words = [word for word in words if word != ""]

    return " ".join(words)


print(reverse_words(input3))
