class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        i = 1

        m = max(arr) + k

        l = 0

        while i <= m and k != 0:
            if l < len(arr) and i == arr[l]:
                l += 1
            else:
                k -= 1
            i += 1
        return i - 1
            