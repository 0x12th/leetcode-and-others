"""
[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
[[]] -> []
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        result = merged = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next

        merged.next = list1 or list2

        return result.next

    def merge_k_lists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            result = lists[0]
        for _ in range(1, len(lists)):
            result = self.merge_two_lists(result, lists[_])
        return result
