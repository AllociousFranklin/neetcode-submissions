class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_score = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                height = min(heights[i], heights[j])
                volume = width * height

                max_score = max(max_score, volume)
        return max_score
