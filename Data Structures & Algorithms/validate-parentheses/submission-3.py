class Solution:
    def isValid(self, s: str) -> bool:
        end = { ')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in end.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last != end[c]:
                    return False
        
        return True if not stack else False
