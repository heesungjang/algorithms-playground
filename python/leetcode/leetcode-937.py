from pprint import pprint


def reorder_log_files(logs):
    # lists to store string logs and number logs
    letters, digits = [], []

    # iterate through each logs
    for log in logs:
        if log.split()[1].isdigit():
            # if digit log, append to digits
            digits.append(log)
        else:
            # if letter log, append to letters
            letters.append(log)

    # at this point, all letter logs and digits logs are seperated

    # sort letter logs by given condition
    # 1. letters-logs are sorted lexicographically by contents
    # 2. if contents are the same, then sort them by their identifier

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    # letters are sorted
    # digit logs come after letter logs, thus extend
    letters.extend(digits)

    return letters


result = reorder_log_files(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])

print(result)
