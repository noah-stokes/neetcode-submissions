class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        can = nums[0]
        for num in nums:
            if num == can:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                can = num

        return can