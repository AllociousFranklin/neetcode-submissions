class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        for i in range (len(heights)):
            for j in range(i+1, len(heights)):
                width = j -i
                height = min(heights[i], heights[j])
                result.append(width * height)
        return max(result)