# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        values = []
        current = lists

        for i in lists:
            current = i
            while current is not None:
                values.append(current.val)
                current = current.next
        sorted_values = sorted(values)

        result = None
        current1 = None
        for i in sorted_values:
            newNode = ListNode(i)
            if result is None:
                result = newNode
                current1 = newNode
            else:
                current1.next = newNode
                current1 = current1.next
                
        return result

        