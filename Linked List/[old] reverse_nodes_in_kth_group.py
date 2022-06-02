# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def traverse(self, head):
        if not head:
            return []
        
        return [head.val] + self.traverse(head.next)
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        items = self.traverse(head)
        
        val = []
        n = len(items)
        
        for i in range(n):
            val.append(items[i])
            
            if (i + 1) % k == 0:
                values.append(val)
                val = []
            elif i + 1 == n:
                values.append(val)
                
        
        
        for i in range(len(values)):
            if len(values[i]) == k:
                values[i] = values[i][::-1]
        
        values = [value for item in values for value in item]
        
        # print(values)
        
        root = None
        current = None
        for val in values:
            if not root:
                root = ListNode(val)
                current = root
            else:
                current.next = ListNode(val)
                current = current.next
        
        return root
            
        
            
        
            
                
            
            
            
        
    
        