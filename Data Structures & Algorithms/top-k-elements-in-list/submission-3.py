class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency  = Counter(nums)
        minHeap = []
        for key,v in frequency.items():
            if len(minHeap)<k:
                heapq.heappush(minHeap,[v,key])
            else:
                heapq.heappushpop(minHeap,[v,key])
        return [value[1] for value in minHeap]
                