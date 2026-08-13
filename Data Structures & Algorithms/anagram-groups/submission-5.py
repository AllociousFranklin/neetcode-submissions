class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            # 1. Your exact character counting logic from Valid Anagram
            t_hash = {}
            for char in word:
                t_hash[char] = 1 + t_hash.get(char, 0)
            
            # 2. Convert the dictionary into a tuple of pairs so it can be a key
            # Example: {'e': 1, 'a': 1, 't': 1} becomes (('a', 1), ('e', 1), ('t', 1))
            key = tuple(sorted(t_hash.items()))
            
            # 3. Your grouping logic
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
                
        return list(group.values())
