class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        current = {}

        for r in range(len(s)):
            while s[r] in current:
                current.pop(s[l])
                l += 1
            current[s[r]] = 0
            length = r - l + 1
            if length > longest:
                longest = length

        return longest





        
