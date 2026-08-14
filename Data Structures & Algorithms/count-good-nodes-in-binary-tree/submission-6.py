# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #dfs cuz saw "#goodNodes", root of tree to node "
        def dfs(node, maxVal):
            if not node:
                return 0
            # update maxVal
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            # dfs left & right
            res = res + dfs(node.left, maxVal) + dfs(node.right, maxVal) 
            return res

        return dfs(root, root.val)