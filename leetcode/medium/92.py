"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverse_between(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        if head is None or left == right:
            return head

        dummy = ListNode(0, head)
        prev: ListNode = dummy

        for _ in range(left - 1):
            assert prev.next is not None
            prev = prev.next

        current = prev.next
        assert current is not None

        for _ in range(right - left):
            next_node = current.next
            assert next_node is not None
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
