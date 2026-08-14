# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def dfs(cur):
            nonlocal count, ans
            if not cur or ans is not None:
                return
            dfs(cur.left)
            count+=1
            if count == k:
                ans = cur.val

            dfs(cur.right)
        dfs(root)
        return ans