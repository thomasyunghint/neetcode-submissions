# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, h: Optional[ListNode]) -> bool:
        s, f = h, h
        
        while h:
            if f.next == None or f.next.next == None:
                return False
            s = s.next
            f = f.next.next
            if s.val == f.val:
                return True
        return False
