class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        min_count = float('inf') 
        total = 0
        #sliding window
        for r in range(len(nums)):
            # add new
            total += nums[r]
            # if >= target -> trim window
            while total >= target:
                min_count = min(min_count, r-l+1)
                total -= nums[l]
                l += 1
            
        return min_count if min_count <= len(nums) else 0