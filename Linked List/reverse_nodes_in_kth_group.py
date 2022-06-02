# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head, k):
        
        if not head:
            return head
        
        current = head
        prev = None
        next = None
        count = 0
        
        # validate do we have k elements in head or not
        while current is not None and count < k:
            current = current.next
            count += 1

        if count != k:
            return head
        else:
            current = head
            count = 0
        
        
        # reverse first kth nodes
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
            
        # next kth group
        if next is not None:
            # head was always on the first element and after reverse the first element became the kth element with next = None so next batch address to pass in the next of head
            head.next =  self.reverse(next, k)
        
        # return the head
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        root = self.reverse(head, k)
        return root
        