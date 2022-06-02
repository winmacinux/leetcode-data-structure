# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getKey(node):
    return node.val
    
class Solution:
        
    def traverse(self, l):
        if not l:
            return []

        return [l] + self.traverse(l.next)        
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = self.traverse(list1) + self.traverse(list2)
        result.sort(key=getKey)
        
        for i in range(len(result) - 1):
            result[i].next = result[i+1]
            
        if len(result):
            return result[0]
        else:
            return None