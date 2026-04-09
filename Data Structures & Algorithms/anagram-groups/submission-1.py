class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        i = 0
        newArr = []
        while i < len(strs):
            j = ''.join(sorted(strs[i]))
            if j in dict:
                newArr = []
                k = 0
                while k<len(strs):
                    place= "".join(sorted(strs[k]))
            
                    if place == j:
                        newArr.append(k)
                        k=k+1
                    else:
                        k=k+1
                dict[j]= newArr
            else:
                newArr = []
                newArr.append(i)
                dict[j]=newArr
            i= i+1
        
        newArr = []
        for key, value in dict.items():
            newArr.append(value)
        
        i =0
        while i < len(newArr):
            j=0
            while j <len(newArr[i]):
                newArr[i][j]=strs[newArr[i][j]]
                j=j+1
            i=i+1
        return newArr
        
        
        