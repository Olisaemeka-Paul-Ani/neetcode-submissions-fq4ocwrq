class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        minHeap = []
        i = 0
        while i < len(points):
            value=(-(math.sqrt((points[i][0])**2+(points[i][1])**2)))
            if len(minHeap) < k:
                heapq.heappush(minHeap,[value, i])
                i = i+1
            else:
                heapq.heappushpop(minHeap,[value, i])
                i = i+1
        output = []
        for x , v in minHeap:
            output.append(points[v])
        return output
        