class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketSort = [0]*(len(nums)+1)
        frequency = Counter(nums)
        for key,value in frequency.items():
            if bucketSort[value]==0:
                bucketSort[value] = [key]
            else:
                bucketSort[value].append(key)
            
        i = len(bucketSort)-1
        l=0
        answer = []
        while i >=0:
            if l==k:
                break
            if bucketSort[i] != 0:
                answer.extend(bucketSort[i])
                l=l+len(bucketSort[i])
                i= i-1
            else:
                i=i-1
        return answer
        
            