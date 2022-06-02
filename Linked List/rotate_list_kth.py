# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        l = 1
        
        # validate whether list is not blank or single element
        if not current or not current.next:
            return head
        
        # go to the last element
        while current.next:
            current = current.next
            l += 1
        
        # form a circular loop
        current.next = head
        
        # get remaining rotation after a complete cycle rotation
        if k >= l:
            k = k%l
        
        # rotate to the remaining items: len - k
        i = 0
        while i < l - k:
            current = current.next
            i += 1
            
        # set head to start point
        # set current as last point
        head = current.next
        current.next = None
        
        return head
            
        
        
            
        
            
            
            