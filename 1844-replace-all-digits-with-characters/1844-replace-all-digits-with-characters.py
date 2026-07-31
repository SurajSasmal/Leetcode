class Solution:
    def replaceDigits(self, s: str) -> str:
        
        c = ""
        
        n = len(s)

        for i in range(n):
            if '0' <= s[i] <= '9':
                c += chr(ord(s[i-1]) + int(s[i]))
            else:
                c += s[i]
        return c