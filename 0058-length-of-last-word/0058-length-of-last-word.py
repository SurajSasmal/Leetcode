class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # words = s.split()

        # return len(words[-1])

        # other way 

        count = 0

        right = len(s) - 1

        while right >= 0 and s[right] == " ":
            right = right - 1
        while right >= 0 and s[right] != " ":
            count = count + 1
            right = right - 1

        return count