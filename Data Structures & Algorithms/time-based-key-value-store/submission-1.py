from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.kv=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        arr=self.kv[key]
        l,r=0,len(arr)-1
        ans=""
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid][1]<=timestamp:
                ans=arr[mid][0]
                l=mid+1
            else:
                r=mid-1
        
        return ans
            

