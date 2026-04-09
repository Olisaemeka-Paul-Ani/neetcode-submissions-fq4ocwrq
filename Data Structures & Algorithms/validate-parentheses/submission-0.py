class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        i = 0
        stack =["*"]
        dictionary = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        "*" : 1

        }

        while i < len(s):
            if s[i] == "(" or s[i] == "["  or s[i] == "{":
                stack.append(s[i])
                i = i+1
            elif dictionary[stack[len(stack)-1]] != s[i]:
                return  False
            else:
                stack.pop()
                i = i+1
        if stack != ["*"]:
            return False
        return True

            