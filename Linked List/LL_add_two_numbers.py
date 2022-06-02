# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def sumListValues(self, l):
        if not l:
            return ''
        return str(l.val) + self.sumListValues(l.next)
                
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = int(str(self.sumListValues(l1))[::-1])
        val2 = int(str(self.sumListValues(l2))[::-1])
        result =  str(val1 + val2)
        root = None
        for char in result:
            root = ListNode(int(char), root)
        return root
            