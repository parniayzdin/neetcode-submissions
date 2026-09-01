# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #give priority to smaller numbers
        result = None
        current = None
        pq = []
        for i in range(len(lists)):
            node = lists[i]
            if node is not None:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        while pq:
            #the node that had the smallest value
            value, i, smallest = heapq.heappop(pq)
            
            if result is None:
                result = smallest
                current = smallest
            else:
                current.next = smallest
                current = current.next
            #we need to attach the node that contains the smallest value
            nextNode = smallest.next

            if nextNode:
                heapq.heappush(pq, (nextNode.val, i, nextNode))

        return result

        