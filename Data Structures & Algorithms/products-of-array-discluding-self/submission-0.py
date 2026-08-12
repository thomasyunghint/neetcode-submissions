class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create res array [1] *nums
        res = [1]*len(nums)
        #1st pass: left to right
        for i in range(1,len(nums)):
        # store product of all elements to left 
        # of i
        # res_i = res_i-1 * nums_i-1
            res[i] = res[i-1]*nums[i-1]
        #2nd pass: right to left
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
        # store product of all elements to right
        # of i
        # postfix (update for next leftwards element)
        # res_i *=postfix 
            res[i] *=postfix
        # postfix *= nums_i
            postfix*= nums[i]
        #return res
        return res