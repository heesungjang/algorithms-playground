nums = [1, 1, 1, 2, 2, 3]

k = 2


def topKFrequent(nums, k):
    dic = {}
    answer = []

    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: -item[1])[:k]}

    for k, v in dic.items():
        answer.append(k)

    return answer


assert topKFrequent(nums, k) == [1, 2]
assert topKFrequent([1], 1) == [1]
