class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #hashmap
        dp= [-1]*(len(nums)+1)
        #dfs
        def dfs(i):
            #if in: return
            if dp[i] != -1:
                return dp[i]
            best=1
            # loop element from i+1 to end:
            for j in range(i+1, len(nums)): 
                # if its value is larger, update best = itself or 1+dfs(that)
                if nums[i] < nums[j]:
                    best = max(best, 1 + dfs(j))
            #store in dp
            dp[i] = best
            #return
            return best
        #return max(dfs(i)) start from any index
        return max(dfs(i) for i in range(len(nums)+1))