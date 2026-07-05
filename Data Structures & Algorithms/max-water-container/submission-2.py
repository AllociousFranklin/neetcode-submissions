class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_score = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            volume = width * height
            max_score = max(max_score, volume)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_score
