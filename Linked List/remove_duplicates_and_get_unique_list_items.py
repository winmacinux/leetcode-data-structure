# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ref = {}
        
        current = head
        
        while current:
            key = current.val
            if key in ref:
                ref[key] = ref[key] + 1
            else:
                ref[key] = 1
            current = current.next
            
        root = None
        current = None
        for (key, count) in ref.items():
            if count == 1:
                if not current:
                    current = ListNode(key)
                    root = current
                else:
                    current.next = ListNode(key)
                    current = current.next
        
        return root