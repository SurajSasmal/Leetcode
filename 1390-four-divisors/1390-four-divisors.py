class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        totalSum = 0

        for number in nums:

            count = 0
            total = 0

            i = 1

            while i * i <= number:

                if number % i == 0:

                    divisor1 = i
                    divisor2 = number // i

                    if divisor1 == divisor2:

                        count += 1
                        total += divisor1
                    else:
                        count += 2
                        total += divisor1 + divisor2
                
                if count > 4:
                    break
                
                i += 1
            
            if count == 4:
                totalSum += total
        
        return totalSum
        