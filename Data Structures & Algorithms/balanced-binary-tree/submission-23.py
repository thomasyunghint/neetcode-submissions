# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Ba = True
        def dfs(i):
            nonlocal Ba
            if not i:
                return 0
            l = dfs(i.left)
            r = dfs(i.right)
            if abs(l-r) > 1:
                Ba = False
            return 1 + max(l, r)
        dfs(root)
        return Ba