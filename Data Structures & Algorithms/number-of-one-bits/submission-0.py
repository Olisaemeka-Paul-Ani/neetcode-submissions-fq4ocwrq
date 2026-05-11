class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n:
            if n%2:
                output = output+1
            n = n >> 1
        return output
        
        