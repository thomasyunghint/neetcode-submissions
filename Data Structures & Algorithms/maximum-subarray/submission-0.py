class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxCur = -1
        for n in nums:
            if total < 0:
                total = 0
            total += n
            maxCur = max(maxCur, total)
        return maxCur