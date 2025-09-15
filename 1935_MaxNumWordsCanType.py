class Solution:
    # PASS: 0ms, 17.9MB
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        br_letter = set(brokenLetters)
        count , isTrue = 0, True
        for i in text:
            if i in br_letter:
                isTrue = False
            elif i == " ":
                if isTrue:
                    count += 1
                else:
                    isTrue = True

        if isTrue and text[-1] != " ":
            count += 1

        return count
