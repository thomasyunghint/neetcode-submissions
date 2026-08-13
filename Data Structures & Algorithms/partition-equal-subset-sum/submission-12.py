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
        for i in range(len(nums)-1, -1, -1):
            next_dp = set()
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                next_dp.add(t+nums[i])
                next_dp.add(t)
            dp = next_dp
        return True if target in dp else False