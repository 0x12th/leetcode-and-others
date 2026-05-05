"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        prev_pnt, crt_pnt = None, head  # previously and current pointers
        while crt_pnt:
            next_pnt = crt_pnt.next
            crt_pnt.next = prev_pnt
            prev_pnt = crt_pnt
            crt_pnt = next_pnt
        return prev_pnt
