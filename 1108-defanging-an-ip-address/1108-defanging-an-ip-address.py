class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        s = ""

        for ch in address:
            if ch == '.':
                s += '[.]'
            else:
                s += ch
        return s