class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        i=j=0
        counterOne = Counter(s1)
        counterTwo = collections.defaultdict(int)
        while j < len(s2):
            counterTwo[s2[j]]=counterTwo[s2[j]]+1
            while j-i+1 > len(s1):
                counterTwo[s2[i]]=counterTwo[s2[i]]-1
                if counterTwo[s2[i]]==0:
                    counterTwo.pop(s2[i])
                i=i+1
            if counterTwo == counterOne:
                return True
            j=j+1
        return False
        