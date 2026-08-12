class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create res array [1] *nums
        res = [1] * (len(nums))
        prefix=1
        #1st pass: left to right
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res