class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                cur = prices[r] - prices[l]
                best = max(best, cur)
            else:
                l = r
            r += 1
        
        return best