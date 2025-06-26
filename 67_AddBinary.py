# 1ms
def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = ""
        len_a, len_b = len(a), len(b)
        while True:
            if len_a <= 0 and len_b <= 0:
                if carry == "1":
                    return "1" + result
                return result
            num_a = a[len_a - 1] if len_a > 0 else "0"
            num_b = b[len_b - 1] if len_b > 0 else "0"
            if num_a == "1" and num_b == "1":
                if carry == "1":
                    result = "1" + result
                    carry = "1"
                else:
                    result = "0" + result
                    carry = "1"
            elif num_a != num_b :
                if carry == "1":
                    result = "0" + result
                    carry = "1"
                else:
                    result = "1" + result
                    carry = ""
            else:
                if carry == "1":
                    result = "1" + result
                    carry = ""
                else:
                    result = "0" + result
            len_a -= 1
            len_b -= 1


print(addBinary(None, "11", "1"))
