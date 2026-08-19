class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            #base: if in dp -> return itself
            if (i,total) in dp:
                return dp[(i,total)]
            # if i reach end ->  if total == target -> return 1 else 0
            if i == len(nums):
                res = 1 if total == target else 0
                dp[(i,total)] = res
                return res
            #try add or sub
            add = dfs(i+1, total+nums[i])
            sub = dfs(i+1, total-nums[i])
            #save in dp
            dp[(i,total)] = add + sub
            #return
            return dp[(i,total)]
        
        return dfs(0,0)