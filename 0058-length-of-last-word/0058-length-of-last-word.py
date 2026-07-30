class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count_last = 0

        n = len(s) - 1

        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':

            count_last += 1
            n -= 1
        
        return count_last 

