class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []

        for i in range(len(matrix)):

            min_value = min(matrix[i])
            col = matrix[i].index(min_value)
            is_lucky = True

            for j in range(len(matrix)):
                if matrix[j][col] > min_value:
                    is_lucky = False
                    break
            if is_lucky:
                ans.append(min_value)
        return ans
