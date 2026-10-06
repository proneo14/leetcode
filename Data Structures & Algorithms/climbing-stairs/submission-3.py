class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}

        def helper(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2

            if n in seen:
                result = seen[n]
            else:
                result = helper(n - 1) + helper(n - 2)
            
            seen[n] = result
            return result

        return helper(n)