class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h_set = {}
        for i, num in enumerate(numbers):
            compliment = target - num

            if compliment in h_set:
                return [h_set[compliment] + 1, i + 1]
            h_set[num] = i    


        