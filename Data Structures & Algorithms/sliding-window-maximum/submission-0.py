class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=j=0
        q = collections.deque()
        output = []
        while j < len(nums):
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)
            
            if i > q[0]:
                q.popleft()
            
            if j-i+1 >=k:
                output.append(nums[q[0]])
                i=i+1
            j=j+1
        return output
            
        