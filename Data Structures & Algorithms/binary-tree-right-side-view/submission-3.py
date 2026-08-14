# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        res=[]
        q=deque([root])

        while q:
            qLen = len(q)
            rside=0
            for i in range(qLen):
                node = q.popleft()
                if node:
                   rside=node.val
                   q.append(node.left)
                   q.append(node.right)
            if rside:
                res.append(rside)
        return res