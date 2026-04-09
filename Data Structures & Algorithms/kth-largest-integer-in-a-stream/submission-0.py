class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.minHeap = []
        self.kthEl =0
        
    def getK(self, arr, k):
        i=0
        self.minHeap = []
        while i < len(arr):
            heapq.heappush(self.minHeap, arr[i])
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
            i=i+1
        return self.minHeap[0]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.kthEl = self.getK(self.nums, self.k)
        return self.kthEl
        
