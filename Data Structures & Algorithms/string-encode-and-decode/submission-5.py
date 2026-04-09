class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "wertyhgvcfrtyujhbvcdrftyujhgvcfdrtyh"
        if strs == [""]:
            return ""
        encoder =[]
        i = 0
        while i < len(strs):
            if i == len(strs)-1:
                encoder.extend(list(strs[i]))
                i = i+1
            else:
                encoder.extend(list(strs[i]))
                encoder.append("€")
                i = i+1
        encoder = ''.join(encoder)
        return encoder

    def decode(self, s: str) -> List[str]:
        if s == "wertyhgvcfrtyujhbvcdrftyujhgvcfdrtyh":
            return []
        if s == "":
            return [""]
        decoder =[]
        placeHolder =""
        i = 0
        while i < len(s):
            if s == "wertyhgvcfrtyujhbvcdrftyujhgvcfdrtyh":
                return []
            if i == len(s)-1:
                placeHolder = placeHolder + s[i]
                decoder.append(placeHolder)
            if s[i] == "€":
                decoder.append(placeHolder)
                placeHolder =""
                i = i+1
            else:
                placeHolder = placeHolder + s[i]
                i = i+1
        return decoder

