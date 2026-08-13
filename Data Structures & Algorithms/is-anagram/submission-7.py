class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        t_hash = {}
        for char in t:
            t_hash[char] = 1 + t_hash.get(char,0)
        for char in s:
            t_hash[char] = t_hash.get(char,0) - 1
        if set(t_hash.values())<={0}:
            return True
        return False