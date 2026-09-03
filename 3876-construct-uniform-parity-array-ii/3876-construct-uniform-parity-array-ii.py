class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        smallOdd = float('inf')

        for num in nums1:
            if num % 2 == 1:
                smallOdd = min(smallOdd, num)
            
        if smallOdd == float('inf'):
            return True 
        
        for nums in nums1:
            if nums % 2 == 0 and nums <= smallOdd:
                return False
        return True 
        