class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        for key in nums:
            heapq.heappush(minHeap,-key)
        i = 0
        answer = 0
        while i <k:
            answer= -minHeap[0]
            heapq.heappop(minHeap)
            i = i+1
        return answer
            
        