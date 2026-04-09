class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i=longest=output=0
        numSet = set(nums)
        for n in numSet:
            if n-1 not in numSet:
                longest =0
                while n +longest in numSet:
                    longest = longest+1
                output = max(output,longest)
        return output
            