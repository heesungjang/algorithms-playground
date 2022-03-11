# 스파르타 토토리반 운영용 알고리즘 문제 풀이

# 최빈값 찾기
import collections
from pprint import pprint
from string import ascii_lowercase
from typing import List

text = "hello, this is sparta"


def find_max_occurance(text: str) -> str:
    counter = collections.defaultdict(int)

    for char in text:
        if not char.isalnum():
            continue
        else:
            counter[char] += 1

    return max(counter, key=counter.get)


find_max_occurance(text)


def find_number_in_array(nums: List[int], target) -> bool:
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return True

        if mid_value > target:
            right = mid - 1
        elif mid_value < target:
            left = mid + 1

    return False


find_number_in_array([3, 5, 6, 1, 2, 4], 1)


def print_first_occurrence_index(s: str) -> str:
    map = {}
    result = []
    for idx, char in enumerate(s):
        if char in map:
            continue
        else:
            map[char] = idx

    for alphabet in ascii_lowercase:
        if alphabet in map:
            result.append(map[alphabet])
        else:
            result.append(-1)

    print(" ".join(str(num) for num in result))


print_first_occurrence_index("baekjoon")
