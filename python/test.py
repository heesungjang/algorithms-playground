import collections
from typing import List


def group_anagrams(strs: List[str]):
    # default dictionary 리스트 값으로 생성
    dic = collections.defaultdict(list)

    for word in strs:
        # 각 단어를 알파벳 순서로 정렬
        sorted_word = "".join(sorted(word))
        # 정렬된 단어를 키 값으로 아나그램을 그룹핑 한다.
        dic[sorted_word].append(word)

    return list(dic.values())


result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
