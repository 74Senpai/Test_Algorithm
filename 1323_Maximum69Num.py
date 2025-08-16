class Ver1:
    # 0ms, 17.84MB
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == "6":
                return int(num[0: i] + "9" + num[i + 1:])

        return int(num)
    
class Ver2:
    # 0ms, 17.63MB
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        return int(num.replace("6", "9", 1))