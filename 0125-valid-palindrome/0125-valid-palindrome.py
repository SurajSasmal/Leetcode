class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def is_alphanumeric(ch):
            code = ord(ch)
            if 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122:
                return code
        
        while(i < j):
            left = s[i]
            right = s[j]

            if not is_alphanumeric(left):
                i = i + 1
                continue
            if not is_alphanumeric(right):
                j = j - 1
                continue
            if left.lower() != right.lower():
                return False
            i = i + 1
            j = j - 1
        return True