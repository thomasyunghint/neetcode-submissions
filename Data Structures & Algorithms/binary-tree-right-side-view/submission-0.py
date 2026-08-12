# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque([root])

        while q:
            rSide = None
            qLen=len(q)
            for i in range(qLen):
                n = q.popleft()
                if n:
                    rSide = n
                    q.append(n.left)
                    q.append(n.right)
            if rSide:
                res.append(rSide.val)
        return res