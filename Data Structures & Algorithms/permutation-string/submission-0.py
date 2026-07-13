class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash = {}
        window = {}

        # Build frequency maps
        for i in range(len(s1)):
            s1_hash[s1[i]] = s1_hash.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        # Check the first window
        if s1_hash == window:
            return True

        l = 0

        # Slide the window
        for r in range(len(s1), len(s2)):
            # Add new character
            window[s2[r]] = window.get(s2[r], 0) + 1

            # Remove left character
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            l += 1

            # Compare frequency maps
            if window == s1_hash:
                return True

        return False