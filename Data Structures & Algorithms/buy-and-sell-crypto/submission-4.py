class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxdiff = 0
        
        minp = prices[0]
        maxp = 0

        for i in range(len(prices)):
            maxp = prices[i]
            
            if (maxp - minp) > maxdiff:
                maxdiff = maxp - minp
            
            if prices[i] < minp:
                minp = prices[i]


        return maxdiff