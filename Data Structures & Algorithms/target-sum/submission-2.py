class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, total):
            #base: if in dp -> return
            if (i,total) in dp:
                return dp[(i,total)]
            #base: when done all nums
            if i == len(nums):
                return 1 if total == target else 0
            #add & sub
            add = dfs(i+1, total+nums[i])
            sub = dfs(i+1, total-nums[i])
            #save result
            dp[(i,total)] = add+sub
            return dp[(i,total)]
        return dfs(0, 0)
        