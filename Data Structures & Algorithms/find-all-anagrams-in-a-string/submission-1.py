class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        l = len(p)
        freq_p = defaultdict(int)
        for c in p:
            freq_p[c] += 1
        
        res = []
        freq_cur = defaultdict(int)

        for i in range(0, l):
            freq_cur[s[i]] += 1
        
        if freq_cur == freq_p:
            res.append(0)

        for i in range(1, len(s) - l + 1):
            freq_cur[s[i-1]] -= 1
            if freq_cur[s[i-1]] == 0:
                del freq_cur[s[i-1]]

            freq_cur[s[i+l-1]] += 1

            if freq_cur == freq_p:
                res.append(i)
        
        return res
                