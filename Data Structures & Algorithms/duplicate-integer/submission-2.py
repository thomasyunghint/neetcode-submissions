class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, x in enumerate(nums):
            if x in seen:
                return True
            seen[x] = i
        return False