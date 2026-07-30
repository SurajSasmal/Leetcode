class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        answer = 0

        m = len(jewels)

        n = len(stones)

        for i in range(m):
            for j in range(n):
                if jewels[i] == stones[j]:
                    answer += 1
        return answer