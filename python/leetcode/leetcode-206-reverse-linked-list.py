# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            # 포인터 방향 변경
            curr.next = prev
            prev = curr
            curr = next

        return prev
