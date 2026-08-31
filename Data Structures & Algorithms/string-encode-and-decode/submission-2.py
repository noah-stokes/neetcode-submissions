class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "$" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = len(s)
        i = 0
        while i < l:
            j = s.find("$", i)
            size = int(s[i:j])
            nxt = s[j + 1 : j + size + 1]
            decoded.append(nxt)
            i = j + 1 + size
        return decoded



