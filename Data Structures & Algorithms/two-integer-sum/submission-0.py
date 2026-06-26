class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in hash:
                return[hash[check], i]

            hash[num] = i
        