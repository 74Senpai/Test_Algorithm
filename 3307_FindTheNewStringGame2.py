class Ver1:
    # FAILD : TLE 737 / 901 testcases passed
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        operations_len = len(operations)
        word = "a"
        for i in range(k):
            if len(word) >= k:
                break
            if i < operations_len:
                if operations[i] == 0:
                    word += word
                    continue
                for ch in word:
                    if ch == "z":
                        word += "a"
                        continue
                    word+= chr(ord(ch) + 1)
            else:
                break

        return word[k - 1]
    
class Ver2:
    # FAILD : MLE 727 / 901 testcases passed
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        def bitAdd(self, word):
            if word != "":
                if word[-1] != "z":
                    return bitAdd(None, word[0:-1]) + chr(ord(word[-1]) + 1)
                return bitAdd(None, word[0:-1]) + "a"
            return ""
        
        word = "a"
        for i in range(k):
            if len(word) >= k:
                return word[k-1]
            else:
                if operations[i] == 1:
                    word += bitAdd(None, word)
                else:
                    word += word

        
class Ver3: 
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        if all(op == 0 for op in operations):
            return "a"
        word = "a" * (k - 1)
        
        

    
    
