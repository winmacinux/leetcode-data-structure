# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head, start, end):
        prev = None
        current = head
        
        while current and end > 0:
            next = current.next
            if start == 1:
                current.next = prev
                prev = current
            else:
                start = start - 1
            end = end - 1
            current = next
                
        return prev
    
    def toList(self, head):
        current = head
        data = []
        while current:
            data.append(current.val)
            current = current.next
            
        return data
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        data = self.toList(head)
        reverse = self.reverse(head, left, right)
        reverse = self.toList(reverse)

        j = 0
        for i in range(len(data)):
            if i >= left -1 and i <= right -1:
                data[i] = reverse[j]
                j += 1
        
        root = None
        curr = root
        for val in data:
            if not root:
                curr = ListNode(val)
                root = curr
            else:
                curr.next = ListNode(val)
                curr = curr.next
        
        return root
            
            
        