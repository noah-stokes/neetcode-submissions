class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ''
        def backtrack(o, c):
            nonlocal cur
            # n pairs
            if o == c == n:
                res.append(cur)
            
            # add (
            if o < n:
                cur += '('
                backtrack(o + 1, c)
                cur = cur[:-1]
            # add )
            if c < o:
                cur += ')'
                backtrack(o, c + 1)
                cur = cur[:-1]
        
        backtrack(0, 0)
        return res