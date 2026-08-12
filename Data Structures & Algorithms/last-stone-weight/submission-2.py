class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #maxHeap
        stone = [-s for s in stones]
        heapq.heapify(stone)


        #pop 2 heaviest. if 2nd>1st, add diff
        while len(stone)>1:
            first = heapq.heappop(stone)
            second = heapq.heappop(stone)
            if second>first:
                heapq.heappush(stone, first-second)
        
        stone.append(0)
        return abs(stone[0])