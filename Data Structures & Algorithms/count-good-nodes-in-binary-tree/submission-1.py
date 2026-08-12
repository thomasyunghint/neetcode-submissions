# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(n, mVal):
            if not n:
                return 0

            res = 1 if n.val >= mVal else 0
            mVal = max(mVal, n.val)
            res+=dfs(n.left, mVal)
            res+=dfs(n.right, mVal)
            return res
        return dfs(root, root.val)