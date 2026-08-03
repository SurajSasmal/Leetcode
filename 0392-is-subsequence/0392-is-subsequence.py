class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        n = len(s)

        m = len(t)

        i = 0

        j = 0

        while i < n and j < m:

            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] != t[j]:
                j += 1
        
        if i == len(s):
            return True
        else:
            return False
