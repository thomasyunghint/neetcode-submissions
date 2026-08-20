class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] > len(nums) // 2:
                return i