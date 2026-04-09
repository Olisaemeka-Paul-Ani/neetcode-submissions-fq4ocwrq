class TimeMap:

    def __init__(self):
        self.hashMap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        output =""
        values = self.hashMap.get(key,[])
        i=0
        j = len(values)-1
        while i <= j:
            m = (i+j)//2
            if values[m][1] <= timestamp:
                 output = values[m][0]
                 i=m+1
            else:
                j=m-1
        return output


        
