class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0

        l = len(pref)

        for c in words:
            if c[:l] == pref:
                count += 1
        return count