#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None
        
        while current is not None:
            nextNode = current.next #temporarly save the next node
            current.next = prev #temporarily reverse the pointer 
            prev = current
            current = nextNode
        return prev

       