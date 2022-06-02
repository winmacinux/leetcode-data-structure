# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def traverse(self, node):
        if not node:
            return []
        
        return [node.val] + self.traverse(node.next)
    
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
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        flaten = [node for nodes in lists for node in self.traverse(nodes)]
        flaten.sort()
        # print(flaten)
        
        root = None
        head = None
        for val in flaten:
            curr = ListNode(val)
            if not root:
                root = curr
                head = root
            else:
                head.next = curr
                head = curr
        
        return root
        