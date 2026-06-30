class MedianFinder:

    def __init__(self):
        self.l=[]
        
        

    def addNum(self, num: int) -> None:
        
        self.l.append(num)
        self.l.sort()
        

    def findMedian(self) -> float:
        n=len(self.l)
        if len(self.l)%2==0:
            return (self.l[int(n/2)-1]+self.l[int(n/2)])/2
        else:
            return self.l[n//2]
        
        