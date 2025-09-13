class Solution:
    #PASS : 0ms, 17.7MB
    def maxFreqSum(self, s: str) -> int:
        dict_vowel = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}
        dict_other = {"_" : 0}
        for i in s:
            if i in dict_vowel:
                dict_vowel[i] += 1
            else:
                dict_other[i] = dict_other.get(i, 0) + 1
        
        return max(dict_vowel.values()) + max(dict_other.values())
