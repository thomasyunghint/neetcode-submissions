# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, count = 0, 0
        def dfs(n):
            nonlocal res, count
            if not n or count >= k:
                return
            dfs(n.left)
            count+=1
            if count == k:
                res = n.val
                return
            dfs(n.right)
        dfs(root)
        return res
