class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        arr = []

        minNums = min(nums)

        maxNums = max(nums)

        j = 0

        for i in range(minNums,maxNums+1):
            if i != nums[j]:
                arr.append(i)
            else:
                j += 1
        return arr

        