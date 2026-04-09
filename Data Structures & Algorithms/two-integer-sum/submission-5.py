class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap ={}
        i = 0
        while i <len(nums):
            if target-nums[i] in hashMap:
                return[hashMap[target-nums[i]],i]
            else:
                hashMap[nums[i]]=i
                i = i+1
   
            
        