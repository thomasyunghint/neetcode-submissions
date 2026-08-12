class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            #base case n==0
            if n == 0:
                curMin, curMax =1, 1
                continue
            #update curMax, curMin
            tmp = curMax*n
            curMax = max(n, curMax*n, curMin*n)
            curMin = min(n, curMin*n, tmp)
            #update res
            res = max(res, curMax)

        return res