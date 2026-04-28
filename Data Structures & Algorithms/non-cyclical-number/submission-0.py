class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        def squareSum (number):
            output = 0
            i=0
            number = str(number)
            while i < len(number):
                output = output+(int(number[i])*int(number[i]))
                i=i+1
            return output
        while n not in hashSet and n!=1:
            hashSet.add(n)
            n = squareSum(n)
        return n==1


        