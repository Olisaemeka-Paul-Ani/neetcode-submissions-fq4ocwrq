class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        maximum, hashSet = 0, set()
        while j < len(s):
            print(hashSet)
            if s[j] in hashSet:
                while s[j] in hashSet:
                    hashSet.remove(s[i])
                    i = i+1
            hashSet.add(s[j])
            maximum = max(maximum, (j-i)+1)
            j = j+1
            
        return maximum