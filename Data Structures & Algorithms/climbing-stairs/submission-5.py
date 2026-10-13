class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        memo = {}

        def inner(i):
            if i in memo:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1
            
            memo[i] = inner(i + 1) + inner(i + 2)
            return memo[i]

        return inner(0)
