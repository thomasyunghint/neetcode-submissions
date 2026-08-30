class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        total = sum(nums) // 2
        dp = {0}
        for i in range(len(nums)):
            haha = set()
            for element in dp:
                haha.add(element)
                haha.add(element + nums[i])
            dp = haha
        return True if total in dp else False