class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        
        return heapq.nlargest(k, counts.keys(), key=counts.get)