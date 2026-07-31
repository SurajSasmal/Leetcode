class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        answer = -1

        for c in sentences:

            great = c.split()

            m = len(great)

            if answer < m:
                answer = m
        return answer