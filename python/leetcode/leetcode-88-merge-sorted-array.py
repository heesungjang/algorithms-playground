input1 = [1, 2, 3, 0, 0, 0]
input2 = [2, 5, 6]
m1 = 3
n1 = 3


def merge(nums1, m, nums2, n):
    last = m + n - 1

    # merge in reverse order
    # nums2 elements to the end of nums1
    while m > 0 and n > 0:
        if nums1[m - 1] < nums2[n - 1]:
            nums1[last] = nums2[n - 1]
            n -= 1
        else:
            nums1[last] = nums1[m - 1]
            m -= 1
        last -= 1

    # fill nums1 with leftover nums2 elements at the beginning
    # this is because elements leftover in nums2 are smaller than any values in nums1
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


merge(input1, m1, input2, n1)
