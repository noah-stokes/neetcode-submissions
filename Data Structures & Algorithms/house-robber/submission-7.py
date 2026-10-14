class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        rob2 = nums[n-1]
        rob1 = max(nums[n-2], rob2)

        for i in range(n-3, -1, -1):
            temp = rob1
            rob1 = max(nums[i] + rob2, rob1)
            rob2 = temp
        
        return rob1
