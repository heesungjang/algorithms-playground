strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs):
    dic = {}
    for str in strs:
        sorted_str = "".join(sorted(str))

        if sorted_str in dic:
            dic[sorted_str].append(str)
        else:
            dic[sorted_str] = [str]

    answer = []

    for value in dic.values():
        answer.append(value)

    return answer


groupAnagrams(strs)
