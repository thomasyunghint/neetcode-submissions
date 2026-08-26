class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        min_count = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_count = min(min_count, r - l + 1)
                total -= nums[l]
                l += 1
        return min_count if min_count <= len(nums) else 0