class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, total):
            if (i,total) in dp:
                return dp[(i,total)]
            #if reach end 
                # if total = target, 1 else 0; add in dp also
            if i == len(nums):
                res = 1 if total == target else 0
                dp[(i,total)] = res
                return res
            #add and sub
            add = dfs(i+1, total+nums[i])
            sub = dfs(i+1, total-nums[i])
            dp[(i,total)] = add+ sub
            return dp[(i,total)]
        return dfs(0,0)