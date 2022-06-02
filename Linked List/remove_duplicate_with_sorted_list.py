# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref = set()
        current = head
        while current:
            ref.add(current.val)
            current = current.next
            
        ref = list(ref)
        ref.sort()
        root = None
        curr = None
            
        for val in ref:
            if not curr:
                curr = ListNode(val)
                root = curr
            else:
                curr.next = ListNode(val)
                curr = curr.next
                
        return root
            
            
        