class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}
        def inner(n):
            if n == 1 or n == 0:
                return 1
            if n in seen:
                return seen[n]
            seen[n] = inner(n-1) + inner(n-2)        
            return seen[n]
        return inner(n)