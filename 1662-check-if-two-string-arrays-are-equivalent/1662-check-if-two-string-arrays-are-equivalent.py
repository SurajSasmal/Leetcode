class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        sentence1 = "".join(word1)

        sentence2 = "".join(word2)

        n = len(sentence1)
        m = len(sentence2)

        if n != m:
            return False 
        
        i = 0
        j = 0
        while i < n:

            if sentence1[i] != sentence2[j]:
                return False
            else:
                j += 1
            i += 1
        return True 
