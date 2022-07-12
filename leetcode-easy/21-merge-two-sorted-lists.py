# [1,2,4], [1,3,4] -> [1, 1, 2, 3, 4, 4]


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = merged = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                merged.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged.next = ListNode(list2.val)
                list2 = list2.next
            merged = merged.next

        while list1:
            merged.next = ListNode(list1.val)
            list1 = list1.next
            merged = merged.next

        while list2:
            merged.next = ListNode(list2.val)
            list2 = list2.next
            merged = merged.next

        return result.next
