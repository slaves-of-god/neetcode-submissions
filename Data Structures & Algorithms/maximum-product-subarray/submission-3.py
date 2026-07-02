class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod,maxprod=1,1
        ans=nums[0]
        for x in nums:
            newmin=min(x,x*minprod,x*maxprod)
            newmax=max(x,x*minprod,x*maxprod)

            
            maxprod=newmax
            minprod=newmin
            ans=max(ans,maxprod)
        return ans
        