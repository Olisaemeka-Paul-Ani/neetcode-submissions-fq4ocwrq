class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i=0
        output = [0]*len(temperatures)
        stack = deque()

        while i < len(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                output[stack[-1][0]] = i- stack[-1][0]
                stack.pop()
            stack.append([i,temperatures[i]])
            i=i+1
        return output
        