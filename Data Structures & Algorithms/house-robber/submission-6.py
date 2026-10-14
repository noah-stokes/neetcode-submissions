class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}

        def inner(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return 0

            memo[i] = max(nums[i] + inner(i + 2), inner(i + 1))

            return memo[i]
        
        return inner(0)

