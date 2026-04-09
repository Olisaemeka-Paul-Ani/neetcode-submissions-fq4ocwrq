class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i=0
        stack = []
        while i < len(tokens):
            if tokens[i] == "+":
                stack.append(stack.pop()+stack.pop())
            elif tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())
            elif tokens[i] == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            elif tokens[i] == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            else:
                stack.append(int(tokens[i]))
            i=i+1
        return stack[0]
        
        
        