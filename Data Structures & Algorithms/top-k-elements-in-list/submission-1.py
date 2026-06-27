class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        buckets = [[] for i in range (len(nums)+1)]

        for num, count in freq_dict.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets)-1, 0,-1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

