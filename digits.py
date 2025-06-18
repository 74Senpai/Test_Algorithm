def plusOne(self, digits: list[int]) -> list[int]:
    if len(digits) == 0: 
        return []
    if digits[-1] != 9:
        digits[-1] = digits[-1] + 1
    else:
        len_digits = len(digits)
        if len_digits == 1 :
            digits[0] = 0
            digits.insert(0,1)
            return digits
        i = 1
        while True:
            digits[-i] = 0
            if i == len_digits:
                digits.insert(0,1)
                break
            i = i + 1 
            if digits[-i] != 9:
                digits[-i] = digits[-i] + 1
                break
    return digits

plusOne = plusOne(None, [9, 9])
print(plusOne)  # Output: [1, 0, 0, 0]