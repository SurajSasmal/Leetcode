class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()

        ans = []
        m = len(potions)

        for spell in spells:

            required = (success + spell - 1) // spell

            l = 0
            r = m

            while l < r:
                mid = (l + r) // 2

                if potions[mid] >= required:
                    r = mid
                else:
                    l = mid + 1

            ans.append(m - l)

        return ans