class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxdiff = 0
        minp = prices[0]

        for i in range(len(prices)):
            if (prices[i] - minp) > maxdiff:
                maxdiff = prices[i] - minp
            
            if prices[i] < minp:
                minp = prices[i]

        return maxdiff