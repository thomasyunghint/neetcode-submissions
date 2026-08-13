class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #memoization
        #base: 0 left
        dp = {0:1}
        #get all combinations
        for total in range(1, target+1):
            dp[total] = 0
            #try all n in nums
            for n in nums:
                dp[total] += dp.get(total-n, 0)
        #return largest problem
        return dp[target]