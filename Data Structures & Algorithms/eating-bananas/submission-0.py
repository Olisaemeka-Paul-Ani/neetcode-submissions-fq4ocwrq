class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        output = max(piles)
        while l <=r:
            k=(l+r)//2
            hours =0
            for p in piles:
                hours = hours + math.ceil(p/k)
            if hours <= h:
                output = min(output,k)
                r=k-1
            else:
                l=k+1              
        return output

        