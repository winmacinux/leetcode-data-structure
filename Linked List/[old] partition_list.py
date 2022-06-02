# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        before = []
        after = []
        
        curr = head
        flag = False
        
        # If empty or single element
        if not head or not head.next:
            return head
        
        # find x head and split between before and after
        while curr:
            if not flag:
                if curr.val == x:
                   flag = True 
                else:
                    before.append(curr.val)
            else:
                if curr.val >= x:
                    after.append(curr.val)
                else:
                    before.append(curr.val)
            curr = curr.next
            
        print(before, after)

        # shift elements from before
        read = len(before) -1
        write = len(before) - 1
        
        while read >= 0:
            if before[read] >= x:
                # split in 2 parts
                s1 = before[:read]
                s2 = before[read+1:write+1]
                s3 = before[write+1:]
                before = s1 + s2 + [before[read]] + s3
                write -= 1
            read -= 1

        if flag:
            values = before + [x] + after
        else:
            values = before + after
        
        root = None
        curr = root
        for val in values:
            if not curr:
                curr = ListNode(val)
                root = curr
            else:
                curr.next = ListNode(val)
                curr = curr.next
                
        return root
            
        
            
            
        