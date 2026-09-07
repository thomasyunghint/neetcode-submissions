# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        count = 0
        def dfs(i, curMax):
            nonlocal count
            if not i:
                return
            if i.val >= curMax:
                count += 1
            curMax =  max(curMax, i.val)
            dfs(i.left, curMax)
            dfs(i.right,curMax)
        dfs(root, root.val)
        return count