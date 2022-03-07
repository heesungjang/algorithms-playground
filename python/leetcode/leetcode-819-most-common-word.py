import collections
import re
from typing import List


def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', " ", paragraph)
        .lower().split()
             if word not in banned]

    # words = re.sub(r'[^\w]', " ", paragraph).lower().split()
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]


p = "Bob hit a ball, the hit BALL flew far after it was hit."

b = ["hit"]

most_common_word(p, b)
