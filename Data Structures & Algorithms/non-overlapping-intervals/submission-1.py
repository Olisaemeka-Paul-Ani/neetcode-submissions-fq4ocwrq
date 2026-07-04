class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output = []
        i=0
        intervals.sort(key = lambda x: x[0])
        while i < len(intervals ):
            if output and output[-1][1] > intervals[i][0]:
                if output[-1][1]> intervals[i][1]:
                    output.pop()
                else:
                    intervals[i] =0
            if intervals[i]:
                output.append(intervals[i])
            i=i+1

        return len(intervals)-len(output)

         