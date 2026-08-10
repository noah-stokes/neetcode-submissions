class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = nums[0]
        for num in nums:
            if num < s:
                s = num
        return s