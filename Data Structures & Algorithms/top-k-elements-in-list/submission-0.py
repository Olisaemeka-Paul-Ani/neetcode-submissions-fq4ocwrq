class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        occurence = list(nums.values())
        occurence.sort(reverse = True)
        highestOccur =[]
        i=0
        while k >0:
            highestOccur.append(occurence[i])
            i=i+1
            k=k-1
        i = 0
        answer = []
        for keys in nums.keys():
            if nums[keys] in highestOccur:
                answer.append(keys)
        return answer
        