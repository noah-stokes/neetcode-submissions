class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0

        for num in seq:
            if (num - 1) not in seq:
                length = 1
                while (num + length) in seq:
                    length += 1
                res = max(length, res)
        return res 

            

