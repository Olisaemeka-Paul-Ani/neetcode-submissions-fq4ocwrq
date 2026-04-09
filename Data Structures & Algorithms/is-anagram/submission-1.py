class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS ={}
        dicT ={}
        s = list(s)
        t = list(t)
        i=0
        while i < len(s):
            if s[i] in dicS:
                dicS[s[i]]= dicS[s[i]]+1
                i=i+1
            else:
                dicS[s[i]]=1
                i=i+1
        
        i=0
        while i < len(t):
            if t[i] in dicT:
                dicT[t[i]]= dicT[t[i]]+1
                i=i+1
            else:
                dicT[t[i]]=1
                i=i+1
        i=0
        if len(s) != len(t):
            return False
        else:
            while i < len(s):
                if s[i] not in dicT:
                    return False
                elif dicS[s[i]] != dicT[s[i]]:
                    return False
                else:
                    i=i+1
            return True
                        