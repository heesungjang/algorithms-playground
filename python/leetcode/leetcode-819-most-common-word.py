import collections
from typing import List

a = "Bob hit a ball, the hit BALL flew far after it was hit."


def most_common_word(paragraph: str, banned: List[str]) -> str:
    # replace := 문자열 치환후, 새로운 문자열 반환
    for c in "!?',;.": paragraph = paragraph.replace(c, " ")

    words = [word for word in paragraph.lower().split() if word not in banned]

    counter = collections.Counter(words)

    return counter.most_common(1)[0][0]


result = most_common_word(a, ["hit"])
print(result)
