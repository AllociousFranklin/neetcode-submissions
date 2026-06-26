class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        S_hash, T_hash = {}, {}
        for i in range(len(s)):
            S_hash[s[i]] = 1 + S_hash.get(s[i], 0 )
            T_hash[t[i]] = 1 + T_hash.get(t[i], 0 )

        for ch in S_hash:
            if S_hash[ch] != T_hash.get(ch, 0 ):
                return False
        return True