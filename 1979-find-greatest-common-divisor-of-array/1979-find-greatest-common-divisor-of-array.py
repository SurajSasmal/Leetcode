class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest = max(nums)

        smallest = min(nums)

        # while smallest != 0:
        #     rem = largest % smallest
        #     largest = smallest 
        #     smallest = rem 
        # return largest

        return gcd(largest,smallest)