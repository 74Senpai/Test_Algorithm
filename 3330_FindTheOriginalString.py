class Ver1:
    # PASS : 41ms, 17.78 MB 
    def possibleStringCount(self, word: str) -> int:
        counter = 1
        for i in range(1 , len(word)):
            if word[i] == word[i - 1]:
                counter += 1

        return counter