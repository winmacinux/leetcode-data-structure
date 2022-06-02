# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution:
        
    def merge(self, h1, h2):
        if not h1:
            return h2
        
        if not h2:
            return h1
        
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h1, h2.next)
            return h2
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = self.merge(list1, list2)
        
        return head