class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        res = defaultdict(list)
        while i < len(strs):
            count = [0]*26
            j = 0
            while j<len(strs[i]):
                count[ord(strs[i][j])-ord("a")]+=1
                j =j+1
            res[tuple(count)].append(strs[i])
            i=i+1
        
        return list(res.values())
        