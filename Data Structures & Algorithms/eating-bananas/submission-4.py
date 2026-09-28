class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        res = 0
        l = 1
        r = m

        while l <= r:
            mid = (r + l) // 2

            cur_t = 0
            for pile in piles:
                cur_t += math.ceil(float(pile) / mid)
            if cur_t <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            
