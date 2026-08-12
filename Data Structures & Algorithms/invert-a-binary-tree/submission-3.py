# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        if not r:
            return None

        tmp = r.right
        r.right = r.left
        r.left = tmp

        self.invertTree(r.left)
        self.invertTree(r.right)

        return root
        