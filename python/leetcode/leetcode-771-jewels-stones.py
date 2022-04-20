import collections


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    # 해쉬 맵 선언
    # count := 보석 갯수
    # count = 0
    #
    # counter = collections.Counter(stones)
    #
    # for char in jewels:
    #     count += counter[char]
    #
    # return count

    count = sum([s in jewels for s in stones])
    print(count)


result = num_jewels_in_stones("aA", "aAAbbbb")
print(result)
