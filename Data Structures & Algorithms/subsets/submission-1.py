class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        
        cur = []
        def dfs(i):
            if i == l:
                res.append(cur[:])
                return

            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            dfs(i + 1)
        
        dfs(0)
        return res



            
