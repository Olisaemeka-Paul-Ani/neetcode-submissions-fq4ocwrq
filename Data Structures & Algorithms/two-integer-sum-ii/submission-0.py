class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while i < j:
            if i != j and numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] < target:
                i=i+1
            elif numbers[i]+numbers[j] > target:
                j=j-1
            else:
                j=j-1
        