class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsTwo = [1]
        while len(digits) != len(digitsTwo):
            digitsTwo.append(0)
        digits.reverse()
        i=carry = 0
        output = []
        valOne = digits[i]
        valTwo = digitsTwo[i]

        while valOne != None or valTwo != None or carry:
            valOne = digits[i] if i < len(digits) else 0
            valTwo = digitsTwo[i] if i < len(digitsTwo) else 0

            value = valOne + valTwo + carry
            carry = value//10
            output.append(value%10)
            i=i+1
            valOne = digits[i] if i < len(digits) else None
            valTwo = digitsTwo[i] if i < len(digitsTwo) else None

        output.reverse()
        return output
        