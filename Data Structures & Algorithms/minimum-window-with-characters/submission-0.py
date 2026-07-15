class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_hash = {}
        for i in range(len(t)):
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)
        have = 0
        need = len(t_hash)
        l = 0   
        result = ""
        result_len = float("inf")
        window = {}
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in t_hash and window[s[r]] == t_hash[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < result_len:
                    result = s[l:r+1]
                    result_len = r-l+1
                window[s[l]] -= 1

                if s[l] in t_hash and window[s[l]] < t_hash[s[l]]:
                    have -=1

                l +=1
        return result