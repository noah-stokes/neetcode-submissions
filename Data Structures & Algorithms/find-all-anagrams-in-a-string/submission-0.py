class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        freq_p = defaultdict(int)
        for c in p:
            freq_p[c] += 1
        
        res = []
        for i in range(len(s)):
            if i + l > len(s):
                break

            cur = s[i:i+l]
            freq_cur = defaultdict(int)
            for c in cur:
                freq_cur[c] += 1

            valid = True
            for c in cur:
                if freq_cur[c] != freq_p[c]:
                    valid = False

            if valid:
                res.append(i)
        
        return res
                