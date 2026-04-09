class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split(' ')
        s = ''.join(s)
        s = s.lower()
        s = list(s)
        i = 0
        while i < len(s):
            if not s[i].isalnum():
                s.remove(s[i])
            else:
                i = i+1
        s = ''.join(s)
        i = 0
        j = len(s)-1
        while i <j  :
            if s[i] != s[j]:
                return False
            else:
                i = i+1
                j = j-1
        return True

            
   
        