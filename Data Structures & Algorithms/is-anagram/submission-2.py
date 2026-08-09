class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for x in s:
            if x in d1:
                d1[x] = d1[x] + 1
            else:
                d1[x] = 0
        
        for x in t:
            if x in d2:
                d2[x] = d2[x] + 1
            else:
                d2[x] = 0

        return d1 == d2
