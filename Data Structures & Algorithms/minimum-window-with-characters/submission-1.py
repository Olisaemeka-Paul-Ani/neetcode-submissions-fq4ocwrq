class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        outputLen, output = float("infinity"), [-1,-1]
        i=j=0
        have = 0
        need = len(Counter(t))
        counterS= collections.defaultdict(int)
        counterT = Counter(t)
        while j < len(s):
            counterS[s[j]]=counterS[s[j]]+1
            if s[j] in counterT and counterS[s[j]]==counterT[s[j]]:
                have = have + 1
            while have == need:
                if j-i+1 < outputLen:
                    outputLen = j-i+1
                    output = [i,j]
                counterS[s[i]]=counterS[s[i]]-1
                if s[i] in counterT and counterS[s[i]]<counterT[s[i]]:
                    have = have-1
                i=i+1
            j=j+1
        if outputLen == float("infinity"):
            return ""
        i,j = output
        return s[i:j+1]

            
        