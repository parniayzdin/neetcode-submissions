# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 

        #find the middle
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        #split the linked list
        if prev is not None:
            prev.next = None
        
        #reverse the second half
        prev1 = None
        while slow is not None:
            nextNode = slow.next
            slow.next = prev1
            prev1 = slow
            slow = nextNode

        #merge linked lists
        dummy = ListNode()
        tail = dummy
        p1 = head 
        p2 = prev1 #reversed second half
        
        while p1 is not None and p2 is not None:
            tail.next = p1
            p1 = p1.next
            tail = tail.next
            tail.next = p2
            p2= p2.next
            tail = tail.next
        if p1 is not None:
            tail.next = p1
        elif p2 is not None:
            tail.next = p2
    
            