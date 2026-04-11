class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast: ListNode | None = dummy
        slow: ListNode | None = dummy

        for _ in range(n + 1):
            if fast is None:
                return head
            fast = fast.next

        while fast is not None:
            fast = fast.next
            assert slow is not None
            slow = slow.next

        assert slow is not None and slow.next is not None
        slow.next = slow.next.next
        return dummy.next
