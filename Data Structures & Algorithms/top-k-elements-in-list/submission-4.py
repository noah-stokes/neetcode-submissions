class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make frequency table
        f = {}
        for n in nums:
            f[n] = 1 + f.get(n, 0)
        # sort based on frequency
        a = []
        for n, v in f.items():
            a.append([v, n])
        
        a.sort()
        # pop to new array k times
        res = []
        for n in range(k):
            res.append(a.pop()[1])
        

        return res