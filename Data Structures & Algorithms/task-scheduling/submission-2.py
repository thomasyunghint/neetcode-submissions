class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-n for n in count.values()]
        heapq.heapify(maxHeap)

        time=0
        q=deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            #if q's time == time, pop back to maxheap
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time