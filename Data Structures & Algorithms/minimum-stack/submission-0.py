class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal,val)
        self.minStack.append(self.minVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.minVal = self.minStack[-1] if self.stack else float("inf")
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()