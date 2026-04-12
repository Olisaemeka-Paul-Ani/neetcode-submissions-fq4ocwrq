class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = []

        for key, value in counter.items():
            heapq.heappush(maxHeap, -value)
        q = deque()
        time =0
        while maxHeap or q:
            time = time+1
            if maxHeap:
                count = 1+maxHeap[0]
                heapq.heappop(maxHeap)
                if count:
                    q.append([count,time+n])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap,q.popleft()[0] )

        return time
        