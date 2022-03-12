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
    slow = head
    fast = head

    # fast at the end or at None position
    # for what? find the middle, cut the linked list into half
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # None at the end (1 -> 2 -> 2 -> 1 -> None)
    # 2 -> 1 -> None
    prev_node = None
    curr_node = slow
    while curr_node is not None:
        next_node = curr_node.next
        # 포인터 방향이 변하는 지점.
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    left, right = head, prev_node

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


print(is_palindrome(head))
