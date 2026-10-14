class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], nums[1], nums[2])

        rob2 = nums[n-1]
        rob1 = max(nums[n-2], rob2)

        for i in range(n-3, 0, -1):
            temp = rob1
            rob1 = max(nums[i] + rob2, rob1)
            rob2 = temp
        
        res1 = rob1

        rob2 = nums[n-2]
        rob1 = max(nums[n-3], rob2)

        for i in range(n-4, -1, -1):
            temp = rob1
            rob1 = max(nums[i] + rob2, rob1)
            rob2 = temp
        
        res2 = rob1

        return max(res1, res2)


