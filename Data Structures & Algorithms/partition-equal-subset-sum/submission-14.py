class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #odd = false
        if sum(nums)%2:
            return False

        #base case
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            nextDp=set()
            for t in dp:
                #add now and next
                nextDp.add(t)
                nextDp.add(t+nums[i])            
            #update dp
            dp = nextDp

        #return if True in else false
        return True if target in dp else False