# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        

        current1 = head
        count = 0
        while current1 is not None:
            current1 = current1.next
            count += 1

        if count == 1:
            return None
        if count == n:
            nextNode= head.next  
            head = None
            return nextNode

        current2 = head 
        count2 = 0
        while count2 < (count - n)-1: #count - n gives you the index you want to delete so you have to subtract by 1
            current2 = current2.next
            count2 +=1
        current2.next = current2.next.next
        return head


        



        