class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = Counter(nums)
        res = []
        for k, v in seen.items():
            if v > 1:
                res.append(k)
        
        return res
