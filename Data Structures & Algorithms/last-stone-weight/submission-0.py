class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap =[]
        i=0
        while i < len(stones):
            heapq.heappush(maxHeap, -stones[i])
            i=i+1
        
        while len(maxHeap) > 1:
            first = -(heapq.heappop(maxHeap))
            second = -(heapq.heappop(maxHeap))

            if first > second:
                heapq.heappush(maxHeap, -(first-second))

        if not maxHeap:
            return 0
        return -maxHeap[0]