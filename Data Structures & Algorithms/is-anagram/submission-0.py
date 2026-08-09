class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        dict[tuple(sorted(s))] = []
        if tuple(sorted(t)) in dict.keys():
            return 'true'
        return 'false'