class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min=prices[0]
        for i in range(1,len(prices)):
            diff=prices[i]-min
            profit=max(profit,diff)
            if prices[i]<min:
                min=prices[i]
        return profit
        