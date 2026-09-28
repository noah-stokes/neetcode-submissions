class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_s1, freq_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1
       
        l = 0

        matches = 0
        for i in range(26):
            if freq_s1[i] == freq_s2[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            i1 = ord(s2[r]) - ord('a')
            freq_s2[i1] += 1

            if freq_s1[i1] == freq_s2[i1]:
                matches += 1
            elif freq_s1[i1] == freq_s2[i1] - 1:
                matches -= 1

            i2 = ord(s2[l]) - ord('a')
            freq_s2[i2] -= 1
            l += 1

            if freq_s1[i2] == freq_s2[i2]:
                matches += 1
            elif freq_s1[i2] == freq_s2[i2] + 1:
                matches -= 1

        return matches == 26
        



