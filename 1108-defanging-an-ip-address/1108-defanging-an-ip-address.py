class Solution:
    def defangIPaddr(self, address: str) -> str:

        newAddress = ' '

        for s in address:
            if s == '.':
                newAddress = address.replace(".","[.]")
        
        return newAddress