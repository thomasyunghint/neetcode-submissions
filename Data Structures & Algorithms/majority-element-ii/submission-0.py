class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        nums.sort()

        for n in nums:
            count[n] = count.get(n, 0)+1
            if n not in res:
                if count[n] > math.floor(len(nums)/3):
                    res.append(n)
        return res