class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[min]
            if profit > max_profit:
                max_profit = profit
            if prices[i] < prices[min]:
                min = i
        return max_profit
        