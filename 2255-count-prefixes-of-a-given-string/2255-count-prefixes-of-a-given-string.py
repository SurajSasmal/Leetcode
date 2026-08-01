class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        n = len(s) 

        m = len(words)

        count = 0
        i = 1

        while i <= n:

            const = s[:i]

            for j in range(m):
                if const == words[j]:
                    count += 1
            i += 1
            
        return count
