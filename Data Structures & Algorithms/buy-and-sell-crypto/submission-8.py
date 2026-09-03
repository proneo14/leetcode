class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxdiff = 0
        minp = prices[0]

        for price in prices:
            if (price - minp) > maxdiff:
                maxdiff = price - minp
            
            if price < minp:
                minp = price

        return maxdiff