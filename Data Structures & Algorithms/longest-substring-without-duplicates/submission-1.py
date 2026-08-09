class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        current = set()

        for r in range(len(s)):
            while s[r] in current:
                current.remove(s[l])
                l += 1
            current.add(s[r])
            longest = max(longest, r - l + 1)
        return longest





        
