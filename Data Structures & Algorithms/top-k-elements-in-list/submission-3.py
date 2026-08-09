class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        arr = []
        for c, v in d.items():
            arr.append([v, c])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

    