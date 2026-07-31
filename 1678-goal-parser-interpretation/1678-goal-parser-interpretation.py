class Solution:
    def interpret(self, s: str) -> str:
        
        # return command.replace('()','o').replace('(al)','al')

        d = {"(al)":"al","()":"o","G":"G"}

        tmp = ""

        result = ""

        for i in range(len(s)):
            tmp += s[i]

            if tmp in d:
                result += d[tmp]
                tmp = ""
        return result
