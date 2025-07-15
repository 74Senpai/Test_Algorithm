class Solution:
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
