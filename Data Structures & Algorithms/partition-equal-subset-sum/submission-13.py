class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # odd = false
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        dp = set() # make it set cuz we want to store all combination in
        #base case
        dp.add(0)
                   # if target in set then True else False

        #many subproblems since want sum
        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for t in dp:
                nextDp.add(t+nums[i])
                nextDp.add(t)
            dp=nextDp

        return True if target in dp else False