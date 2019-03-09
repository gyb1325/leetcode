class Solution:

    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        width = len(height) - 1
        max_area = 0
        for w in range(width, 0, -1):
            max_area = max(max_area, w * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
