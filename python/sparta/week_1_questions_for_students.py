# 스파르타 토토리반 운영용 알고리즘 문제 풀이

# 최빈값 찾기
import collections
from pprint import pprint

text = "hello, this is sparta"


def find_max_occurance(text: str) -> str:
    counter = collections.defaultdict(int)

    for char in text:
        if not char.isalnum():
            continue
        else:
            counter[char] += 1

    return max(counter, key=counter.get)


pprint(find_max_occurance(text))
