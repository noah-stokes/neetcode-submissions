class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(i, s, path):
            if i >= len(nums):
                return
            if s == target:
                res.append(path[:])
                return
            if s > target:
                return
            
            # s < target
            # try current number
            path.append(nums[i])
            dfs(i, s + nums[i], path)
            path.pop()

            # try next
            dfs(i + 1, s, path)
        
        dfs(0,0,[])
        return res



        
        