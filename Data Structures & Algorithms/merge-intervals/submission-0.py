class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        minHeap,i,sortedInt = [], 0, []
        while i < len(intervals):
            heapq.heappush(minHeap, [intervals[i][0], intervals[i][1] ])
            i=i+1
        while minHeap:
            placeHolder = heapq.heappop(minHeap) 
            sortedInt.append(placeHolder) 
        i=0
        output =[ ]
        while i < len(sortedInt):
            a = output[-1][0]  if output else None
            b = output[-1][1]  if output else None
            c = sortedInt[i][0]
            d = sortedInt[i][1]
             

            if output and  max(a,c)<=min(b,d) :
                 
                 
                placeHolder = [min(a,c), max(b,d)]
                 
                output.pop( )
                output.append(placeHolder)
                sortedInt[i] =0
            if   sortedInt[i]: 
                
                output.append(sortedInt[i]) 
            i=i+1
        return output

            

        