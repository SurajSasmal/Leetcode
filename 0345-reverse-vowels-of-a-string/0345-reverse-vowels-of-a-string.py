class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)

        l = 0

        r = len(s) - 1
        vowels = "aeiouAEIOU"

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r] , s[l]
                l = l + 1
                r = r - 1
            elif s[l] not in vowels:
                l = l + 1
            elif s[r] not in vowels:
                r = r - 1

        return "".join(s)
