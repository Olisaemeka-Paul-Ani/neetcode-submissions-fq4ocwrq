class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        minHeap = []
        for t,v in nums.items():
            heapq.heappush(minHeap,[v,t]) 
        i = 0
        n= len(minHeap)
        answer =[]
        k=k 
        while i < n-k:
            heapq.heappop(minHeap)
            i=i+1


        answer = []
        i=0
        while i <len(minHeap):
            answer.append(minHeap[i][1])
            i=i+1
        return answer
            
            