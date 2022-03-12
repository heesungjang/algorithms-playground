from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


input = [1, 2, 2, 1]

curr = temp = ListNode()

for num in input:
    curr.next = ListNode(num)
    curr = curr.next

head = temp.next


def is_palindrome(head: ListNode) -> bool:
    rev = None
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next

        # temprev = rev
        # rev = slow
        # slow = slow.next
        # rev.next = temprev
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next

    return not rev


is_palindrome(head)
