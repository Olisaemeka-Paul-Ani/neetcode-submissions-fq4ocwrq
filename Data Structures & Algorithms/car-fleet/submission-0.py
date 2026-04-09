class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashMap = collections.defaultdict(int)
        i=0
        while i < len(position):
            hashMap[position[i]] = speed[i]
            i=i+1
        speed = []
        position.sort(reverse = True)
        i=0
        while i < len(position):
            speed.append(hashMap[position[i]])
            i=i+1
        aloneTime = []
        i=0
        while i < len(position):
            aloneTime.append((target-position[i])/speed[i])
            i=i+1
        stack = []
        i=0
        while i < len(aloneTime):
            while stack and stack[-1] >= aloneTime[i]:
                aloneTime[i] = stack[-1]
                stack.pop()
            stack.append(aloneTime[i])
            i=i+1
        return len(stack)
        