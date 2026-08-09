class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict.keys():
                return [dict[diff], i]
            dict[n] = i
        
        
        
        