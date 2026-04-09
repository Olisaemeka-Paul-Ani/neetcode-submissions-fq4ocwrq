class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=j=maxCount=output=0
        hashMap = collections.defaultdict(int)
        while j < len(s):
            hashMap[s[j]]=hashMap[s[j]]+1
            maxCount = max(maxCount,hashMap[s[j]])
            while j-i+1-maxCount > k:
                hashMap[s[i]]=hashMap[s[i]]-1
                if hashMap[s[i]]==0:
                    hashMap.pop(s[i])
                i=i+1
            output = max(output,j-i+1)
            j=j+1
        return output