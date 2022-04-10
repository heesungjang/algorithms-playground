from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # 포인터 기법을 사용하기 위해서 배열을 먼저 정렬 한다.
    nums.sort()

    sums = []

    for i in range(len(nums) - 2):
        # i가 0보다 큰데 즉, 두번째 index 부터 이전에 같은 값이 이미 나온 중복 값인지 체크를 한다.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    sums.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1

    return sums


a = three_sum([-1, 0, 1, 2, -1, -4])
print(a)
