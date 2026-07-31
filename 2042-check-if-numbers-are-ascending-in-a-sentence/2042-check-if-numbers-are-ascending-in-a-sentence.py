class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        s = s.split()

        lis = []

        for token in s:
            if token.isdigit():
                lis.append(token)
        
        m = len(lis)

        j = 0 
        k = 1

        while k < m:
            if int(lis[k]) > int(lis[j]):
                j += 1
            else:
                return False
            k += 1
        return True 
