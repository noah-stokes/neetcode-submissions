class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, s, start):
            if s == target:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if s + nums[i] > target:
                    continue
                path.append(nums[i])
                s += nums[i]
                backtrack(path, s, i)
                s -= nums[i]
                path.pop()
        backtrack([], 0, 0)
        return res