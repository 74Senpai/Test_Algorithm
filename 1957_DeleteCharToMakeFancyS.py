class Ver1:
    #PASS : 220 ms ,18.90MB
    def makeFancyString(self, s: str) -> str:
        output = s[:2]
        for i in s[2:]:
            if i == output[-1] and i == output[-2]:
                continue
            output += i
        return output
    
    