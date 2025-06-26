class Ver1:
    # 14ms, 18MB
    def rotatedDigits(self, n: int) -> int:
        result = 0
        rotated_dict = { 50 : 53, 53: 50, 54 : 57, 57 : 54 } 
        for i in range(n + 1):
            str_num = str(i)
            if "3" in str_num or "4" in str_num or "7" in str_num:
                continue
            if str_num != str_num.translate(rotated_dict):
                result += 1

        return result
    
class Ver2:
    # 7ms / 17.7 mb
    def rotatedDigits(self, n: int) -> int:
        result = 0
        for i in range(n + 1):
            str_num = str(i)
            if "3" in str_num or "4" in str_num or "7" in str_num:
                continue
            if "2" in str_num or "5" in str_num or "6" in str_num or "9" in str_num:
                result += 1

        return result