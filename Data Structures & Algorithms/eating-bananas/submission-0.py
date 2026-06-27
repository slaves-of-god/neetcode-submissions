class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min1=1
        max1=max(piles)
        
        while(min1<max1):
            mid = (max1+min1)//2
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if (hours>h):
                min1=mid+1
            else:
                max1=mid
        return min1
        