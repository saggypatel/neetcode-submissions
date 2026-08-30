class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            minH = min(heights[l], heights[r])
            maxW = minH * (r-l)
            result = max(result, maxW)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result