class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        i = 0
        while  i < len(nums):
            print(dict)
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]]=1
                i=i+1
        return False