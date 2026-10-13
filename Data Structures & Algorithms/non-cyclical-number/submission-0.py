class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            if n in seen:
                return False
            seen.add(n)
            s = 0
            nums = str(n)
            for num in nums:
                if num == '0':
                    continue
                s += int(num) * int(num)
            
            if s == 1:
                return True
            
            n = s
            
