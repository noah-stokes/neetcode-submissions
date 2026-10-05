class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float('-inf')

            m = (l + r) // 2

            ls = 0
            s = 0
            for num in reversed(nums[l:m]):
                s += num
                ls = max(ls, s)

            rs = 0
            s = 0
            for num in nums[m + 1:r + 1]:
                s += num
                rs = max(rs, s)

            return max(
                dfs(l, m - 1),
                dfs(m + 1, r),
                ls + nums[m] + rs
            )

        return dfs(0, len(nums) - 1)