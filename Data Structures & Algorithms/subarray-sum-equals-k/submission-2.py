class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix = {0:1}

        for n in nums:
            #search the past
            curSum += n
            diff = curSum - k
            res += prefix.get(diff, 0)

            #record for future use
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return res