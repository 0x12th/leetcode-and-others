from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur = None, head

        for _ in range(left - 1):
            prev, cur = cur, cur.next

        conn_node, rev_cur = prev, cur

        for _ in range(left - 1, right):
            next_pnt, cur.next = cur.next, prev
            prev, cur = cur, next_pnt

        rev_cur.next = next_pnt

        if conn_node:
            conn_node.next = prev
        else:
            head = prev

        return head
