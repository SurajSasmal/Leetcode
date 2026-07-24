class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s) - 1

        count = 0

        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':
            count += 1
            n -= 1

        return count 