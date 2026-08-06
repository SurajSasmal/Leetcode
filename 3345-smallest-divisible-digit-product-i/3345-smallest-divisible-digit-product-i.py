class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        multi = 1
        m = n 
        while n > 0:
            rem = n % 10 
            multi = multi * rem 
            n = n // 10 
        
        if multi % t == 0:
            return m 
        else:
            return self.smallestNumber(m+1,t)

        for i in range(n,n+100):
            
            multi = 1
            m = i

            while m > 0:
                rem = m % 10
                multi = multi * rem 
                m  = m // 10
            
            if multi % t == 0:
                return i
            