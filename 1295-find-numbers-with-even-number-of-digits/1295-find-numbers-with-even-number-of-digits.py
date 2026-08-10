class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        totalCount = 0

        # for num in nums:
        #     count = 0

        #     while num != 0:
        #         rem = num % 10
        #         count += 1
        #         num = num // 10
        #     if count % 2 == 0:
        #         totalCount += 1
        # return totalCount 

        for num in nums:
            
            length = len(str(abs(num)))

            if length % 2 == 0:
                totalCount += 1
        return totalCount 
        