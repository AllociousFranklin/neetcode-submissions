class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = {}

        for ch in s:
            s_hash[ch] = 1 + s_hash.get(ch, 0)
            
        for ch in t:
            # If the character was never in 's', or we used up its count
            if ch not in s_hash or s_hash[ch] == 0:
                return False
            s_hash[ch] -= 1  # Correct way to subtract 1
            
        return True
