class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(i,currSum,currArr):
            if currSum > target or i >= len(candidates):
                return
            if currSum == target:
                output.append(currArr.copy())
                return
            dfs(i,currSum+candidates[i],currArr+[candidates[i]])
            dfs(i+1,currSum,currArr)

        dfs(0,0,[])
        return output
        