class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #base: if 0 left: 1 then
        dp = {0:1}
        #memoization
        #want all combination (can reuse)
        for total in range(1, target+1):
            dp[total]= 0 # initiate a key
            for n in nums:
                dp[total] += dp.get(total-n,0)
        return dp[target]