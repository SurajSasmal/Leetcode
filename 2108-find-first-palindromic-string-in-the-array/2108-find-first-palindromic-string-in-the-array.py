class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        n = len(words)

        for i in range(n):

            palin = words[i]

            if palin == palin[::-1]:
                return palin
                
        return ""