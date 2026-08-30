class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[target] = 1
        for i in range(target-1,-1,-1):
            for c in nums:
                if i + c <= target:
                    dp[i] += dp[i+c]
        return dp[0]