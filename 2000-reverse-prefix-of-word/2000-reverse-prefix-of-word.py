class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # idx = word.find(ch)

        # if idx == -1:
        #     return word
        
        # return word[:idx+1][::-1] + word[idx+1:]

        arr = list(word)

        idx = word.find(ch)

        if idx == -1:
            return word

        left = 0

        right = idx

        while left < right:
            arr[left] , arr[right] = arr[right] , arr[left]

            left += 1
            right -= 1
        
        return "".join(arr)
