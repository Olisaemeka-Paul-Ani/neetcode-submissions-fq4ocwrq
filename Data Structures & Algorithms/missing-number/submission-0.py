class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        output = (n*(n+1))//2
        i=0
        while i < len(nums):
            output=output-nums[i]
            i=i+1
        return output
        