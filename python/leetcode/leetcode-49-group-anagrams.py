import collections
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = {}
    result = []

    for word in strs:
        key = ("".join(sorted(word)))

        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)

    for (idx, key) in enumerate(anagrams):
        result.append(anagrams[key])

    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(strs))


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

group_anagrams(strs)
