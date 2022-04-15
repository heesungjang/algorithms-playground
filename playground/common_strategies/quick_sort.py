from typing import List


def quick_sort(nums: List[int], low: int, high: int):
    def partition(low, high):
        pivot = nums[high]
        left = low

        for right in range(low, high):
            if nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        nums[left], nums[high] = nums[high], nums[left]
        
        return left

    if low < high:
        # 중앙 정렬된 pivot 위치를 반환 받음
        pivot = partition(low, high)

        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)


nums = [3, 2, 7, 11, 1, 5]
print(nums)
quick_sort(nums, 0, len(nums) - 1)
print(nums)
