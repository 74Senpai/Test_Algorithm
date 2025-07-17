class Ver1:
    # 0 ms, 18MB
    def isValid(self, word: str) -> bool:
        vowels = {"a": "a", "e":"e", "i": "i", "o":"o", "u":"u"}
        ch_count = 0
        have_vowels = False
        have_other_ch = False
        for i in word.lower():
            if i in vowels:
                have_vowels = True
            else:
                if i >= "a" and i <= "z":
                    have_other_ch = True
                elif i < "0" or i > "9":
                    return False
            ch_count += 1

        if ch_count >= 3 and  have_other_ch and have_vowels:
            return True
        return False
    
class Ver2:
    #0ms, 17.60 MB
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = ("a", "e", "i", "o", "u")
        contain_vowels = False
        contain_other_ch = False
        for i in word.lower():
            if i in vowels:
                contain_vowels = True
                continue
            
            if i >= "b" and i <= "z":
                contain_other_ch = True
            elif i < "0" or i > "9":
                return False

        return contain_vowels and contain_other_ch
