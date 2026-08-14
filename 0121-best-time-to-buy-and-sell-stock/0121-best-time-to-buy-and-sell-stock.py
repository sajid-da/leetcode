class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = prices[0]
        profit = 0
        for j in range (1,len(prices)):
            if prices[j]< i:
                i = prices[j]
            elif prices[j] - i> profit:
                profit = prices[j] - i
        return profit
            
                