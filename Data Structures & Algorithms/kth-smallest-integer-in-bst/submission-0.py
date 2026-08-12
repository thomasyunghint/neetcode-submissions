# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt= k
        res = root.val

        def dfs(n):
            nonlocal cnt, res
            if not n:
                return
            dfs(n.left)
            if cnt==0:
                return
            cnt-=1
            if cnt==0:
                res = n.val
                return
            dfs(n.right)
        dfs(root)
        return res