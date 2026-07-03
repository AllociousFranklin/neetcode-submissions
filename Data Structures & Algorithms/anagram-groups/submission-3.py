class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            sorted_array = "".join(sorted(word))

            if sorted_array in group:
                group[sorted_array].append(word)
            else:
                group[sorted_array] = [word]
        return list(group.values())
    