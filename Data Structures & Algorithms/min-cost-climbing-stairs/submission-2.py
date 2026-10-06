class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev = cost[0]
        curr = cost[1]

        for i in range(2, len(cost)):
            nextStep = min(prev, curr) + cost[i]

            prev = curr
            curr = nextStep

        return min(prev, curr)