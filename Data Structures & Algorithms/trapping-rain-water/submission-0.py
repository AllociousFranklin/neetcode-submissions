class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):

            left_max = 0
            for j in range(i):
                left_max = max(left_max,height[j])
            
            right_max = 0
            for j in range(i+1, len(height)):
                right_max = max(right_max, height[j])

            total += max(0,min(left_max,right_max) - height[i])

        return total
        
           