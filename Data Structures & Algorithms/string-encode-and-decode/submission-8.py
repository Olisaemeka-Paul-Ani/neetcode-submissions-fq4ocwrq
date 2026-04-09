class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for element in strs:
            output= output + str(len(element)) + "#" + element
        return output
        

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while  s[j]!= "#":
                j = j+1
            length = int(s[i:j])
            output.append(s[j+1: j+1+length])
            i = j+1 + length
        return output