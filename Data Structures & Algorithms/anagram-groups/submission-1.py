class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = defaultdict(list)
        for s in strs:
            srted = ''.join(sorted(s))
            strmap[srted].append(s)
        return  list(strmap.values())
            