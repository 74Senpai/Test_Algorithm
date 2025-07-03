class Ver1:
    # 7ms >=  <= 10MS , 17.89 MB
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            for char in word:
                if char == "z":
                    word += "a"
                    continue
                word += chr(ord(char) + 1)
        
        return word[k - 1]
        