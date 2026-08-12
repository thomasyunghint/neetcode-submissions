# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n, lo, hi):
            if not n:
                return True
            if not (lo<n.val<hi):
                return False
            return dfs(n.left,lo, n.val) and dfs(n.right, n.val,hi)
        return dfs(root, float("-inf"), float("inf"))