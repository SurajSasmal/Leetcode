class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest = max(nums)

        nums.sort()

        smallest = nums[0]

        while smallest != 0:
            rem = largest % smallest
            largest = smallest 
            smallest = rem 
        return largest