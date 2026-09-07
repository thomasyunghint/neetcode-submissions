# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(i, l, r):
            if not i:
                return True
            if not (l < i.val < r):
                return False
            return dfs(i.left, l, i.val) and dfs(i.right, i.val, r)

        return dfs(root, float('-inf'), float('inf'))