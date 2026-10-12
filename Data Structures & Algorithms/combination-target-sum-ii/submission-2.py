class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        cur = []
        def dfs(i, s):
            if s == target:
                res.append(cur[:])
                return
            if i >= len(candidates):
                return
            if s > target:
                return
            
            # include
            cur.append(candidates[i])
            dfs(i+1,s+candidates[i])
            cur.pop()

            # exclude
            j = i
            while candidates[j] == candidates[i]:
                if j + 1 >= len(candidates):
                    return
                j += 1
            i = j
            dfs(i,s)
        
        dfs(0,0)

        return res