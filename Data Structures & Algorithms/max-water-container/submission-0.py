class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            volume = (r - l) * min(heights[r], heights[l])
            if volume > max_volume:
                max_volume = volume
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_volume