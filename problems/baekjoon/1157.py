from collections import Counter

if __name__ == "__main__":
    word = input().upper()
    chars = list(set(word))

    counter = []
    for char in chars:
        counter.append(word.count(char))

    if counter.count(max(counter)) > 1:
        print("?")
    else:
        max_index = counter.index(max(counter))
        print(chars[max_index])
