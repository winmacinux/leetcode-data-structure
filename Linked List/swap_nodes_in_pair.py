# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def swap(self, head):
        
        if not head:
            return head
        
        if head.next:
            next = head.next.next
            
            temp = head.next
            head.next = self.swap(next)
            temp.next = head
            return temp
        else:
            return head
        
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swap(head)
        
        