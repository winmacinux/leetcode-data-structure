# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head):
        prev = None
        current = head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        return prev
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        root = self.reverse(head)
        print(root)
        return root
            
            
        