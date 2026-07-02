class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash, t_hash = {}, {}

        for ch in s:
            s_hash[ch] = 1 + s_hash.get(ch,0)
        for ch in t:
            t_hash[ch] = 1 + t_hash.get(ch,0)

        return s_hash == t_hash
