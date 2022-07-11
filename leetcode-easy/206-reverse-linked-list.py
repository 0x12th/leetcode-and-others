from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_pnt, crt_pnt = None, head  # previously and current pointers
        while crt_pnt:
            next_pnt = crt_pnt.next
            crt_pnt.next = prev_pnt
            prev_pnt = crt_pnt
            crt_pnt = next_pnt
        return prev_pnt
