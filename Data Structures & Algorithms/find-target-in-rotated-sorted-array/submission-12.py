from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Removed the index check that caused the wrong answer
        
        if target not in nums:
            return -1  # 🛑 If target is missing (like target=2), it stops here and returns -1
            
        for i in range(len(nums)):
            if target == nums[i]:
                res = i
        return res
