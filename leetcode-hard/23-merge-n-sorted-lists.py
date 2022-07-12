# [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
# [[]] -> []


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            result = lists[0]
        for _ in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[_])
        return result
