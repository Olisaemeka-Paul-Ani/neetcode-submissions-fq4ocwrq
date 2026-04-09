class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        dict={}
        while i < len(nums):
            if nums[i] in dict:
                dict[nums[i]] = dict[nums[i]]+1
                i=i+1
            else:
                dict[nums[i]]=1
                i=i+1
        i = 0 
        while i < len(nums):
            if dict[nums[i]]>1:
                return True
            else:
                i=i+1
        return False
            