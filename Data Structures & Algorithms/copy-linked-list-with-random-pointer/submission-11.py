"""
import copy
import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #make copylist
        oldToCopy = {None:None}
        cur = head
        while cur:
            val = Node(cur.val)
            oldToCopy[cur]=val
            cur=cur.next

        cur = head
        #alter copylist
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


        